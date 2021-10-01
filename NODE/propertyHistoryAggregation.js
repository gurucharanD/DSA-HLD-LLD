const fs = require('fs');
const data = require('./propertyHistoryAggregationData.js');
// console.log(data)
function aggregateHistory(propertyHistory) {
    try {
        let aggregatedHistory = [];
        console.time('start aggregation');
        const noOfUnits = 250;
        for (let monthWiseHistory of propertyHistory) {
            // history = history._source;

            const dataSource = monthWiseHistory.dataSource;
            const date = monthWiseHistory.surveyDate.split('-');
            const prevSurveyDate = `${date[0] - 1}-${date[1]}`;
            const currentSurveyDate = `${date[0]}-${date[1]}`;
            let isSameStore = false;
            let isIncluded = true;


            monthWiseHistory.occupancyRate = monthWiseHistory.occupancyRate == null ? 85 : monthWiseHistory.occupancyRate;
            let currentMonthHistory = {
                surveyDate: monthWiseHistory.surveyDate,
                units: noOfUnits,
                rentPerunit: monthWiseHistory.effectiveRentUnitBedAmount,
                occupancyrate: monthWiseHistory.occupancyRate,
                dataSource,
            }

            // case: empty propertyhistory
            if (!aggregatedHistory.length) {
                currentMonthHistory.isSameStore = false;
                currentMonthHistory.isIncluded = isIncluded;
                aggregatedHistory.push(currentMonthHistory);
                continue;
            }

            //check if this first record for this month
            let isThisFirstRecordForThisMonth = aggregatedHistory.some(history => {
                const currentDate = history.surveyDate.split('-');
                return `${currentDate[0]}-${currentDate[1]}` == currentSurveyDate;
            });
            //check if this is an Update
            let isThisAnUpdate = aggregatedHistory.some(history => {
                const currentDate = history.surveyDate.split('-');
                return `${currentDate[0]}-${currentDate[1]}` === currentSurveyDate && history.dataSource === dataSource;
            });
            if (!isThisFirstRecordForThisMonth) {
                currentMonthHistory.isSameStore = calculateSameStore(aggregatedHistory, prevSurveyDate, dataSource);
                if (currentMonthHistory.isSameStore) {
                    updateLastYearRecords(aggregatedHistory, prevSurveyDate, dataSource);
                }
                currentMonthHistory.isIncluded = true;
                aggregatedHistory.push(currentMonthHistory);
                continue;
            } else if (isThisAnUpdate) {
                aggregatedHistory.forEach(history => {
                    const currentDate = history.surveyDate.split('-');
                    if (`${currentDate[0]}-${currentDate[1]}` === currentSurveyDate && history.dataSource == dataSource) {
                        history.surveyDate = currentMonthHistory.surveyDate;
                        history.units = currentMonthHistory.units;
                        history.rentPerunit = currentMonthHistory.rentPerunit;
                        history.occupancyrate = currentMonthHistory.occupancyrate;
                    }
                })
                continue;
            } else {
                //check if other source is samestore
                let isOtherSourceSameStore = aggregatedHistory.some(history => {
                    const currentDate = history.surveyDate.split('-');
                    return `${currentDate[0]}-${currentDate[1]}` === currentSurveyDate && history.dataSource !== dataSource && history.isSameStore;
                })
                if (monthWiseHistory.dataSource == 'Axio') {
                    if (isOtherSourceSameStore) {
                        currentMonthHistory.isSameStore = false;
                        currentMonthHistory.isIncluded = false;
                    } else {
                        let isSameStore = calculateSameStore(aggregatedHistory, prevSurveyDate, dataSource);
                        if (isSameStore) {
                            currentMonthHistory.isSameStore = true;
                            currentMonthHistory.isIncluded = true;
                            updateLastYearRecords(aggregatedHistory, prevSurveyDate, dataSource);
                            updateSameYearRecords(aggregatedHistory, currentSurveyDate, 'Yardi');
                        } else {
                            currentMonthHistory.isSameStore = false;
                            currentMonthHistory.isIncluded = false;
                        }
                    }
                } else {
                    let sameStore = calculateSameStore(aggregatedHistory, prevSurveyDate, dataSource);
                    if (sameStore) {
                        currentMonthHistory.isSameStore = true;
                        currentMonthHistory.isIncluded = true;
                        updateLastYearRecords(aggregatedHistory, prevSurveyDate, dataSource)
                        updateSameYearRecords(aggregatedHistory, currentSurveyDate, 'Axio');
                    } else {
                        if (isOtherSourceSameStore) {
                            currentMonthHistory.isSameStore = false;
                            currentMonthHistory.isIncluded = false;
                        } else {
                            currentMonthHistory.isSameStore = false;
                            currentMonthHistory.isIncluded = true;
                            updateSameYearRecords(aggregatedHistory, currentSurveyDate, 'Axio');
                        }
                    }

                }
                aggregatedHistory.push(currentMonthHistory);
            }
        }
        console.timeEnd('start aggregation');
        return aggregatedHistory;
    } catch (e) {
        console.log('exception in aggregateHistory', e);
        return false;
    }
}


function updateLastYearRecords(aggregatedHistory, prevSurveyDate, dataSource) {
    aggregatedHistory.forEach(history => {
        const currentDate = history.surveyDate.split('-');
        if (`${currentDate[0]}-${currentDate[1]}` === prevSurveyDate) {
            if (history.dataSource == dataSource) {
                history.isIncluded = true;
            } else {
                history.isIncluded = false;
            }
        }
    })
    return;
}

function calculateSameStore(aggregatedHistory, prevSurveyDate, dataSource) {
    for (let history of aggregatedHistory) {
        const currentDate = history.surveyDate.split('-');
        if (`${currentDate[0]}-${currentDate[1]}` === prevSurveyDate && history.dataSource == dataSource) {
            return true;
        }
    }
    return false;
}

// function updateSameYearAxioRecords(aggregatedHistory, currentSurveyDate) {
//     aggregatedHistory.forEach(history => {
//         const currentDate = history.surveyDate.split('-');
//         if (`${currentDate[0]}-${currentDate[1]}` === currentSurveyDate) {
//             if (history.dataSource == 'Axio') {
//                 history.isIncluded = false;
//                 history.isSameStore = false;
//             }
//         }
//     })
//     return;
// }
function updateSameYearRecords(aggregatedHistory, currentSurveyDate, dataSource) {
    aggregatedHistory.forEach(history => {
        const currentDate = history.surveyDate.split('-');
        if (`${currentDate[0]}-${currentDate[1]}` === currentSurveyDate) {
            if (history.dataSource == dataSource) {
                history.isIncluded = false;
                history.isSameStore = false;
            }
        }
    })
    return;
}

let history = aggregateHistory(data.data[0].marketDashboardQueryRes)
// console.log(JSON.stringify(history, undefined, 2))
// aggregateHistory(data[1].marketDashboardQueryRes)

fs.writeFileSync('./history.json', JSON.stringify(history.sort((a, b) => a.surveyDate - b.surveyDate), undefined, 2))