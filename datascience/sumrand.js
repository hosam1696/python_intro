const rand = (start, end) => Math.floor(Math.random() * end) + start
const randomRange = num => Array.from({length: num}, (a, b) => b + rand(10, 25))
const sum = nums => nums.reduce((prev, num) => prev + num, 0)
let nums = randomRange(5)
console.log(sum(nums), nums)
