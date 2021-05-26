function minimumWaitingTime(queries) {
	
	let waiting = 0;
	let totalWaiting = 0;
	
	queries.sort( (a,b) => { return a-b} )
	
	for( let i = 0; i < queries.length-1 ; i++) {
		waiting = waiting + queries[i]
		totalWaiting += waiting
	}
	return totalWaiting;

}

// Do not edit the line below.
exports.minimumWaitingTime = minimumWaitingTime;
