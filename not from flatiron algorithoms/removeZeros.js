const heights = [9, 0, 0, 6, 0, 3, 0, 5]
//    result  = [3, 0, 0, 5, 0, 6, 0, 9]


function removeZeros(array) {
   const sorted = array.filter(num => num != 0).sort()
   const result = array.map(num => {
    if (num == 0) {
        return 0
    } else {
       return num
    }
   })

   return result 
}


console.log(removeZeros(heights))