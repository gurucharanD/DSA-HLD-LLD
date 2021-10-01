function Dumped(event, context) {
    try {
        let payload = event.data.payload;

        payload.lastUpdatedDate = new Date(payload.lastUpdatedDate).getTime();

        let { propertyGoldenId = '', mortgageBroker = '', brokerBuyer = '', brokerSeller = '', transactionSequence = 0 } = { ...payload };

        mortgageBroker = mortgageBroker ? mortgageBroker.toLowerCase() : '';
        brokerBuyer = brokerBuyer ? brokerBuyer.toLowerCase() : '';
        brokerSeller = brokerSeller ? brokerSeller.toLowerCase() : '';

        let isMortgageBanked = mortgageBroker.includes('berkadia');
        let isInvestmentSales = (brokerBuyer.includes('berkadia') || brokerSeller.includes('berkadia'));
        let id = `${propertyGoldenId}-${transactionSequence}`;

        console.log(isMortgageBanked, isInvestmentSales)

        return true;
    } catch (err) {
        return false;
    }
}


let data = [
    {
        "brokerSeller": null,
        "brokerBuyer": null,
        "mortgageBroker": null,
        "propertyGoldenId": "PMST76398",
        "transactionSequence": 1
    },
    {
        "brokerSeller": "Berkadia",
        "brokerBuyer": null,
        "mortgageBroker": "Berkadia",
        "propertyGoldenId": "PMST76398",
        "transactionSequence": 3
    },
    {
        "brokerSeller": null,
        "brokerBuyer": null,
        "mortgageBroker": "GRANDBRIDGE REAL ESTATE",
        "propertyGoldenId": "PMST76398",
        "transactionSequence": 2
    }
]

for (let index = 0; index < data.length; index++) {
    const element = data[index];
    Dumped({
        data: {
            payload: element
        }
    })
}
