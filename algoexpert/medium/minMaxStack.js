// Feel free to add new properties and methods to the class.
class MinMaxStack {
	stack = [];
	minMaxStack = [];

	min = null;
	max = null;
	peek() {
		// Write your code here.
		let length = this.stack.length
		return this.stack[length - 1]
	}

	pop() {
		// Write your code here.
		// 		console.log(this.minMaxStack)
		let popped = this.stack.pop()
		// 		let latestMinMax = this.minMaxStack[this.minMaxStack.length-1]

		// 		if(latestMinMax.min==popped || latestMinMax.max==popped ){
		// 			this.minMaxStack.pop()
		// 		}
		this.minMaxStack.pop()

		return popped;
	}

	push(number) {
		if (this.minMaxStack.length) {

			let latestMinMax = this.minMaxStack[this.minMaxStack.length - 1]
			let min = Math.min(latestMinMax.min, number)
			let max = Math.max(latestMinMax.max, number)

			this.minMaxStack.push({
				min, max
			});
		} else {
			this.minMaxStack.push({
				min: number,
				max: number
			});
		}

		this.stack.push(number)
		return null
	}

	getMin() {
		// Write your code here.
		let latestMinMax = this.minMaxStack[this.minMaxStack.length - 1]
		return latestMinMax.min
	}

	getMax() {
		// Write your code here.
		let latestMinMax = this.minMaxStack[this.minMaxStack.length - 1]
		return latestMinMax.max
	}
}

// Do not edit the line below.
exports.MinMaxStack = MinMaxStack;
