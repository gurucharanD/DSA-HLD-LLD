// let payload = {
//     "marketCode": "35614",
//     "propertyFilter": {
//         "propertySubType": [
//             "Garden"
//         ],
//         "propertyClass": [
//             "1"
//         ],
//         "ranges": [
//             [
//                 "numberUnits",
//                 103,
//                 1003
//             ],
//             [
//                 "yearBuilt",
//                 1949,
//                 2020
//             ],
//             [
//                 "averageRentPerSquareFeetAmount",
//                 0.1,
//                 2.37
//             ]
//         ]
//     },
//     "performanceLayers": [
//         {
//             "isSameStore": true,
//             "dataPoint": "rent"
//         },
//         {
//             "isSameStore": false,
//             "dataPoint": "rent"
//         },
//         {
//             "isSameStore": true,
//             "dataPoint": "occupancy"
//         },
//         {
//             "isSameStore": false,
//             "dataPoint": "occupancy"
//         }
//     ],
//     "demogrpahicsLayers": [
//         "B25119",
//         "B25064",
//         "B25002"
//     ]
// }

// for (let iterator of payload.performanceLayers) {
//     const queryPayload = {
//         marketCode: payload.marketCode,
//         ...payload.propertyFilter,
//         ...iterator,
//     };
//     console.log(queryPayload)

// }
// let trendGraphsResponse = {};

// let trendGrapsData = [
//     {
//         "demographicsTrend": [
//             {
//                 "value": 14365,
//                 "key": "2011"
//             },
//             {
//                 "value": 14984,
//                 "key": "2012"
//             },
//             {
//                 "value": 15087,
//                 "key": "2013"
//             },
//             {
//                 "value": 15684,
//                 "key": "2014"
//             },
//             {
//                 "value": 16082,
//                 "key": "2015"
//             },
//             {
//                 "value": 15877,
//                 "key": "2016"
//             },
//             {
//                 "value": 15795,
//                 "key": "2017"
//             },
//             {
//                 "value": 16321,
//                 "key": "2018"
//             }
//         ],
//         "variableCodeType": "graphAggs-trend-doctorates",
//         "variableCode": "B15002"
//     },
//     {
//         "demographicsTrend": [
//             {
//                 "value": 13013,
//                 "key": "2011"
//             },
//             {
//                 "value": 13029,
//                 "key": "2012"
//             },
//             {
//                 "value": 12804,
//                 "key": "2013"
//             },
//             {
//                 "value": 12457,
//                 "key": "2014"
//             },
//             {
//                 "value": 12813,
//                 "key": "2015"
//             },
//             {
//                 "value": 12704,
//                 "key": "2016"
//             },
//             {
//                 "value": 13317,
//                 "key": "2017"
//             },
//             {
//                 "value": 14148,
//                 "key": "2018"
//             }
//         ],
//         "variableCodeType": "graphAggs-trend-professionals",
//         "variableCode": "B15002"
//     },
//     {
//         "demographicsTrend": [
//             {
//                 "value": 107365,
//                 "key": "2011"
//             },
//             {
//                 "value": 108496,
//                 "key": "2012"
//             },
//             {
//                 "value": 110731,
//                 "key": "2013"
//             },
//             {
//                 "value": 113069,
//                 "key": "2014"
//             },
//             {
//                 "value": 113644,
//                 "key": "2015"
//             },
//             {
//                 "value": 116583,
//                 "key": "2016"
//             },
//             {
//                 "value": 119176,
//                 "key": "2017"
//             },
//             {
//                 "value": 121941,
//                 "key": "2018"
//             }
//         ],
//         "variableCodeType": "graphAggs-trend-bachelors",
//         "variableCode": "B15002"
//     },
//     {
//         "demographicsTrend": [
//             {
//                 "value": 56208,
//                 "key": "2011"
//             },
//             {
//                 "value": 58232,
//                 "key": "2012"
//             },
//             {
//                 "value": 59615,
//                 "key": "2013"
//             },
//             {
//                 "value": 61185,
//                 "key": "2014"
//             },
//             {
//                 "value": 62911,
//                 "key": "2015"
//             },
//             {
//                 "value": 64940,
//                 "key": "2016"
//             },
//             {
//                 "value": 66751,
//                 "key": "2017"
//             },
//             {
//                 "value": 67590,
//                 "key": "2018"
//             }
//         ],
//         "variableCodeType": "graphAggs-trend-masters",
//         "variableCode": "B15002"
//     }
// ]
// console.time('here')

// for (const iterator of trendGrapsData) {
//     const type = iterator.variableCodeType.split('-')[2];
//     for (const trend of iterator.demographicsTrend) {
//         if (!trendGraphsResponse[`${trend.key}`]) {
//             trendGraphsResponse[`${trend.key}`] = []
//         }
//         trendGraphsResponse[`${trend.key}`].push({
//             key: type,
//             value: trend.value
//         })
//     }
// }
// console.log(trendGraphsResponse)

// for (const vintage in trendGraphsResponse) {
//     const total = trendGraphsResponse[`${vintage}`].reduce((accumulator, currentValue) => {
//         return accumulator + currentValue.value
//     }, 0);
//     console.log(vintage, total)
//     trendGraphsResponse[`${vintage}`] = trendGraphsResponse[`${vintage}`].map(x => {
//         return {
//             key: x.key,
//             value: Number(((x.value / total) * 100).toFixed(2))
//         }
//     });
// }

// console.timeEnd('here')

// totalByYear = [
//     {
//         "key": "2011",
//         "doc_count": 4,
//         "val": {
//             "value": 190951
//         }
//     },
//     {
//         "key": "2012",
//         "doc_count": 4,
//         "val": {
//             "value": 194741
//         }
//     },
//     {
//         "key": "2013",
//         "doc_count": 4,
//         "val": {
//             "value": 198237
//         }
//     },
//     {
//         "key": "2014",
//         "doc_count": 4,
//         "val": {
//             "value": 202395
//         }
//     },
//     {
//         "key": "2015",
//         "doc_count": 4,
//         "val": {
//             "value": 205450
//         }
//     },
//     {
//         "key": "2016",
//         "doc_count": 4,
//         "val": {
//             "value": 210104
//         }
//     },
//     {
//         "key": "2017",
//         "doc_count": 4,
//         "val": {
//             "value": 215039
//         }
//     },
//     {
//         "key": "2018",
//         "doc_count": 4,
//         "val": {
//             "value": 220000
//         }
//     }
// ]
// trendGrapsData.forEach((trend) => {
//     trendGraphsResponse[trend.variableCodeType.replace('graphAggs-trend-', '')] = trend.demographicsTrend.map(data => {
//         let total = totalByYear.filter(x => x.key === data.key)
//         return {
//             key: data.key,
//             value: Number(((data.value / total[0].val.value) * 100).toFixed(2))
//         }
//     });
// })

// console.log(trendGraphsResponse)
console.log(a)
let a = 1