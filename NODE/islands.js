// let n = 2
// let islands = ['0011', '0314']
// let ship = [0, 0]
let islands = ['1100', '1223', '3041']
let n = 3
let ship = [0, 4]
let distance = []


for (let i = 0; i < n; i++) {
    let island = (islands[i].split(''))
    let indexes = [
        [parseInt(island[0]), parseInt(island[1])],
        [parseInt(island[2]), parseInt(island[3])],
        [parseInt(island[0]), parseInt(island[3])],
        [parseInt(island[2]), parseInt(island[1])]
    ]
    let minDistance = 1e9 + 7
    for (let j = 0; j < indexes.length; j++) {
        let d = Math.sqrt(Math.abs(((indexes[j][0] - ship[0]) * (indexes[j][0] - ship[0])) + ((indexes[j][1] - ship[1]) * (indexes[j][1] - ship[1]))))
        if (d <= minDistance) {
            minDistance = d
        }
    }
    distance.push({
        index: i + 1,
        distance: minDistance
    })
}
distance = distance.sort((a, b) => a.distance - b.distance)
let sol = ''
for (let k = 0; k < distance.length; k++) {
    sol += distance[k].index + ' '
}
console.log(sol.trim())