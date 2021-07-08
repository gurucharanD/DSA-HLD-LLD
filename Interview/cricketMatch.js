
//   0 1 2 3 4 5 6 7 8 9 10 11
// [ 1, 2, 4, 1, 3, 1, 1, 4, 6, 0, 0, 1, 1, 1, 2, 1, 0, 6, 0, 0, 1, 2, 1, 0, 0, 4, 0, 1, 0 ]
// We are given a ball-by-ball cricket score. Dravid and Sachin are the 2 batsmen playing. Dravid bats the first ball. We have to calculate the total score of both players.
// Note: After odd runs, strike changes, and other player gets to bat. After 6 balls also strike changes. Assume there aren’t any wide/no balls or wickets taken.
 
// Example Input array : 
// [ 1, 2, 4, 1, 3, 1, 1, 4, 6, 0, 0, 1, 1, 1, 2, 1, 0, 6, 0, 0, 1, 2, 1, 0, 0, 4, 0, 1, 0 ]
 
// Example output
// Dravid: 20
// Sachin: 24

function scoring(runs){
  let playerOneScore = 0
  let playerTwoScroe = 0
  
  let onStrike = 'player1'
  
//   playerOneScore += runs[0]
  
  
    
  for(let i = 0;i<runs.length;i++){
    
    let oddRuns = runs[i]%2 !== 0
    let lastBall = (i+1)%6 == 0 ? true : false
    
    if(onStrike == 'player1'){
      playerOneScore += runs[i]
    }else{
       playerTwoScroe += runs[i]
    }
    
    
    if(oddRuns || lastBall ){
      if(onStrike == 'player1'){
           onStrike = 'player2'

      }else{
            onStrike = 'player1'

      }
    } 
    
   
    
  }    
    
    
//     console.log(playerOneScore)
//     console.log(playerTwoScroe)
    return [playerOneScore,playerTwoScroe]

    
  
}

console.log(scoring([ 1, 2, 4, 1, 3, 1, 1, 4, 6, 0, 0, 1, 1, 1, 2, 1, 0, 6, 0, 0, 1, 2, 1, 0, 0, 4, 0, 1, 0 ]))


{ name:'file1', id:1 , folderId:1}
{ name:'file2', id:2 }
{
    fileId:1,
    folderId:1
  }

