function tournamentWinner(competitions, results) {
	
	// [home,away]
	//0 - away team won
	//1 - home team won
  
	let points={};
	let winnerScore = 0;
  let winner='';

	
	for(let i = 0; i<results.length; i++ ){
      
		let game = competitions[i];
      
		if( !points[game[1]] ){
			points[game[1]]=0;
		}
		if( !points[game[0]] ){
			points[game[0]]=0;
		}
      
		if(results[i] == 1){
			points[game[0]]=points[game[0]]+3;
			if(points[game[0]] > winnerScore ){
					winnerScore = points[game[0]]
					winner = game[0];
			}
		} else {
			points[game[1]]=points[game[1]]+3;
			if(points[game[1]] > winnerScore ){
					winnerScore = points[game[1]]
					winner = game[1];
			}
		}
		
	}
  
//   let winner='';
// 	let winnerScore = 0;
	
// 	for(let j in points){
// 		if(points[j] > winnerScore){
//       console.log(j)
//       winnerScore = points[j]
// 			winner = j;
// 		}
// 	}
  
	console.log(points)
  return winner;
		
}

// Do not edit the line below.
exports.tournamentWinner = tournamentWinner;

//better version of above 
function tournamentWinner(competitions, results) {
	
	// [home,away]
	//0 - away team won
	//1 - home team won
  
	let points={};
	let winnerScore = 0;
  let winner='';

	
	for(let i = 0; i<results.length; i++ ){
      
		let game = competitions[i];
		
		let [home,away] = competitions[i];
		
		let currWinner = results[i] == 1 ? home : away;
		
		if(!points[currWinner]){
			points[currWinner]=0;
		}
		
		points[currWinner] = points[currWinner]+3
		
		if( points[currWinner] > winnerScore ){
				winner = currWinner;
				winnerScore = points[currWinner]
		}   		
	}
  

  
	console.log(points)
  return winner;
		
}

// Do not edit the line below.
exports.tournamentWinner = tournamentWinner;

____________PYTHON implemantaion_______________
// def tournamentWinner(competitions, results):
	
// 	scores = {}
// 	for index in range(len(competitions)):
// 		homeTeam = competitions[index][0]
// 		awayTeam = competitions[index][1]
		
// 		result = results[index]
// 		# print(homeTeam,awayTeam,result)
		
// 		if result == 1:
// 			if homeTeam in scores:
// 				scores[homeTeam]+=3
// 			else:
// 				scores[homeTeam]=3
// 		else:
// 			if awayTeam in scores:
// 				scores[awayTeam]+=3
// 			else:
// 				scores[awayTeam]=3
				
// 	winningScore = 0
// 	winner = ''
// 	for player in scores:
// 		if scores[player] > winningScore:
// 			winningScore = scores[player]
// 			winner = player
		
// 	print(scores)
		
//     return winner

