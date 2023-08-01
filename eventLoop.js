let a = Promise.resolve('resolve')

setTimeout(() => {
    console.log("timeout")
}, 0)

process.nextTick(() => {
    console.log("next tick")
    process.nextTick(() => {
        console.log("nested tick")
    })
})
a.then(x => {
    console.log('here', x)
    process.nextTick(() => {
        console.log("nested tick from promise")
    })
})

