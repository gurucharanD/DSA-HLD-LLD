let data = [
    {
        key: 1535760000000,
        key_as_string: '2018-09-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1718.1219868469238,
        },
    },
    {
        key: 1538352000000,
        key_as_string: '2018-10-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1719.2619868469237,
        },
    },
    {
        key: 1541030400000,
        key_as_string: '2018-11-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1718.081996612549,
        },
    },
    {
        key: 1543622400000,
        key_as_string: '2018-12-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1685.0579782104492,
        },
    },
    {
        key: 1546300800000,
        key_as_string: '2019-01-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1684.3099896240233,
        },
    },
    {
        key: 1548979200000,
        key_as_string: '2019-02-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1669.5500119018554,
        },
    },
    {
        key: 1551398400000,
        key_as_string: '2019-03-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1685.0700141906736,
        },
    },
    {
        key: 1554076800000,
        key_as_string: '2019-04-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1684.129992675781,
        },
    },
    {
        key: 1556668800000,
        key_as_string: '2019-05-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1708.9159886169434,
        },
    },
    {
        key: 1559347200000,
        key_as_string: '2019-06-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1708.123985595703,
        },
    },
    {
        key: 1561939200000,
        key_as_string: '2019-07-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1713.0419714355469,
        },
    },
    {
        key: 1564617600000,
        key_as_string: '2019-08-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1719.2760311889647,
        },
    },
    {
        key: 1567296000000,
        key_as_string: '2019-09-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1720.822007598877,
        },
    },
    {
        key: 1569888000000,
        key_as_string: '2019-10-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1721.734011077881,
        },
    },
    {
        key: 1572566400000,
        key_as_string: '2019-11-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1690.690018157959,
        },
    },
    {
        key: 1575158400000,
        key_as_string: '2019-12-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1690.690018157959,
        },
    },
    {
        key: 1577836800000,
        key_as_string: '2020-01-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1689.8920303344726,
        },
    },
    {
        key: 1580515200000,
        key_as_string: '2020-02-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1688.9800268554686,
        },
    },
    {
        key: 1583020800000,
        key_as_string: '2020-03-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1688.9640090942382,
        },
    },
    {
        key: 1585699200000,
        key_as_string: '2020-04-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1687.496030883789,
        },
    },
    {
        key: 1588291200000,
        key_as_string: '2020-05-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1690.2960452270509,
        },
    },
    {
        key: 1590969600000,
        key_as_string: '2020-06-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1684.7719973754884,
        },
    },
    {
        key: 1593561600000,
        key_as_string: '2020-07-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1684.476008758545,
        },
    },
    {
        key: 1596240000000,
        key_as_string: '2020-08-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1714.0859872436524,
        },
    },
    {
        key: 1598918400000,
        key_as_string: '2020-09-01',
        doc_count: 5,
        totalOccupiedUnits: {
            value: 1714.0859872436524,
        },
    },
]
let response = [];

let stopDate = '2019-10-01'

data.every(d => {
    if (d.key_as_string !== stopDate) {
        let nextyearDate = d.key_as_string.split('-')
        nextyearDate = `${+nextyearDate[0] + 1}-${nextyearDate[1]}-${nextyearDate[2]}`
        let nextyearData = data.find(x => x.key_as_string == nextyearDate)
        response.push({
            key: nextyearDate,
            value: Math.ceil(nextyearData.totalOccupiedUnits.value) - Math.ceil(d.totalOccupiedUnits.value)
        })
        return true
    } else {
        return false
    }
})

console.log(response);