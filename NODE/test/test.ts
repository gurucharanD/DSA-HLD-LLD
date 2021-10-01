var temp1 ={
    displayName: "Inventory",
    columnName: null,
    childColumns: [{
      displayName: "Operating Properties",
      columnName:"NumberProps_Operating"
    }, {
      displayName: "Operating Units",
      columnName:"NumberUnits_Operating"
    }, {
      displayName: "Vintage",
      columnName: "DecadeBuilt"
    }]
  }


  var temp= {
    isSelected: true,
    displayName: 'Market KPI',
    columnName: null,
    childColumns: [{
        isSelected: true,
        displayName: 'Market Eff Rent',
        columnName: null,
        childColumns: [{
            isSelected: true,
            displayName: 'Growth (3Yr)',
            columnName: 'MarketEffRentGrowth_3Yr_Unit',
        }]
    }, {
        isSelected: true,
        displayName: 'Market Occupancy Rate',
        columnName: null,
        childColumns: [{
            isSelected: true,
            displayName: 'Growth (3Yr)',
            columnName: 'MarketOccupancyGrowth_3Yr',
        }, {
            isSelected: true,
            displayName: 'Current',
            columnName: 'MarketOccupancyRate',
        }]
    }, {
        isSelected: true,
        displayName: 'Cap Rate',
        columnName: null,
        childColumns: [{
            isSelected: true,
            displayName: 'Trailing 6 Mo. (3Yr Chg)',
            columnName: 'CapRate6moChange_3Yr',
        }, {
            isSelected: true,
            displayName: 'Trailing 6 Mo.',
            columnName: 'CapRate_6mo',
        }, {
            isSelected: true,
            displayName: 'Trailing 12 Mo. (3Yr Chg)',
            columnName: 'CapRate12moChange_3Yr',
        }, {
            isSelected: true,
            displayName: 'Trailing 12 Mo.',
            columnName: 'CapRate_12mo',
        }]
    }, {
        isSelected: true,
        displayName: 'Sale Activity',
        columnName: null,
        childColumns: [{
            isSelected: true,
            displayName: '% Change (3Yr)',
            columnName: 'NumberSalesChange_3Yr',
        }, {
            isSelected: true,
            displayName: 'Trailing 12 Mo. (#)',
            columnName: 'NumberSales',
        }]
    }, {
        isSelected: true,
        displayName: 'Housing Permits',
        columnName: null,
        childColumns: [{
            isSelected: true,
            displayName: 'Growth (3Yr)',
            columnName: 'TotalPermitsGrowth_3Yr',
        }, {
            isSelected: true,
            displayName: 'Annual Total',
            columnName: 'AnnualTotalPermits',
        }]
    }, {
        isSelected: true,
        displayName: 'Market Inventory',
        columnName: null,
        childColumns: [{
            isSelected: true,
            displayName: 'Growth (3Yr)',
            columnName: 'InventoryGrowth_3Yr',
        }]
    }]
}

var count =0;

 function iterating (temp){
    for (var key in temp) {
        // console.log(key, temp[key]);
        if(key==='childColumns'){
            // console.log(key, temp[key]);
            var kk=temp[key];
            for (var keys in kk) {
                // console.log(kk[keys].isSelected);
            if(kk[keys].isSelected){
            console.log(kk[keys].displayName);
            count++;
            if(kk[keys]==='childColumns')
            iterating (kk[keys] );
            }
        }
      } 
    }

 } 





 iterating(temp);
 console.log(count);