const fs = require('fs');
const data = require('./propertyHistoryAggregationData.js');
// console.log(data)
function aggregateHistory(propertyHistory) {
    try {
        let aggregatedHistory = [];
        console.time('start aggregation');
        for (let history of propertyHistory) {
            const noOfUnits = history.numberUnitsBeds;
            // history = history._source;

            const dataSource = history.dataSource;
            const date = history.surveyDate.split('-');
            const prevSurveyDate = `${date[0] - 1}-${date[1]}`;
            const currentSurveyDate = `${date[0]}-${date[1]}`;
            let isSameStore = false;
            let isIncluded = true;


            history.occupancyRate = history.occupancyRate == null ? 85 : history.occupancyRate;
            let currentMonthHistory = {
                surveyDate: history.surveyDate,
                units: noOfUnits,
                rentPerunit: history.effectiveRentUnitBedAmount,
                occupancyrate: history.occupancyRate,
                dataSource,
                //add occupiedUnits,
            }

            // case: empty propertyhistory
            if (!aggregatedHistory.length) {
                currentMonthHistory.isSameStore = isSameStore;
                currentMonthHistory.isIncluded = isIncluded;
                aggregatedHistory.push(currentMonthHistory);
                continue;
            }

            let lastYearCurrentMonthHistory = aggregatedHistory.filter(history => {
                const currentDate = history.surveyDate.split('-');
                return `${currentDate[0]}-${currentDate[1]}` === prevSurveyDate;
            });
            let sameYearCurrentMonthHistory = aggregatedHistory.filter(history => {
                const currentDate = history.surveyDate.split('-');
                return `${currentDate[0]}-${currentDate[1]}` === currentSurveyDate;
            });

            if (dataSource === 'Yardi') {
                let indexOfSameYearSameDataSourceRecord = sameYearCurrentMonthHistory.findIndex(month => month.dataSource === 'Yardi');
                if (indexOfSameYearSameDataSourceRecord !== -1) {
                    aggregatedHistory = aggregatedHistory.filter(history => {
                        const currentDate = history.surveyDate.split('-');
                        return `${currentDate[0]}-${currentDate[1]}` !== currentSurveyDate;
                    });
                    console.log(aggregatedHistory)
                    Object.assign(sameYearCurrentMonthHistory[indexOfSameYearSameDataSourceRecord], currentMonthHistory);
                } else {
                    lastYearCurrentMonthHistory.forEach(monthlyHistory => {
                        if (monthlyHistory.dataSource === dataSource) {
                            monthlyHistory.isIncluded = true;
                            isSameStore = true;
                        } else {
                            monthlyHistory.isIncluded = false;
                        }
                    });
                    sameYearCurrentMonthHistory.forEach(month => {
                        if (month.dataSource == 'Axio') {
                            month.isIncluded = isSameStore ? false : month.isIncluded;
                            month.isSameStore = isSameStore ? false : month.isSameStore;
                        }
                    })
                    aggregatedHistory = aggregatedHistory.filter(history => {
                        const currentDate = history.surveyDate.split('-');
                        return `${currentDate[0]}-${currentDate[1]}` !== prevSurveyDate;
                    });
                    currentMonthHistory.isIncluded = isIncluded;
                    currentMonthHistory.isSameStore = isSameStore;
                    sameYearCurrentMonthHistory.push(currentMonthHistory);
                }
                lastYearCurrentMonthHistory = lastYearCurrentMonthHistory.concat(sameYearCurrentMonthHistory);
                aggregatedHistory = aggregatedHistory.concat(lastYearCurrentMonthHistory);
                continue;
            } else {

            }

        }

        console.timeEnd('start aggregation');

        return aggregatedHistory;
    } catch (e) {
        console.log('exception in aggregateHistory', e);
        return false;
    }
}

let history = aggregateHistory(data.data[1].marketDashboardQueryRes)
// aggregateHistory(data[1].marketDashboardQueryRes)

fs.writeFileSync('./history.json', JSON.stringify(history.sort((a, b) => a.surveyDate - b.surveyDate), undefined, 2))