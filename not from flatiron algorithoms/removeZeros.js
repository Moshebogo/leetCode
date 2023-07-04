const heights = [9, 0, 0, 6, 0, 3, 0, 5]
//    result  = [3, 0, 0, 5, 0, 6, 0, 9]


// this will create a sorted array with no zeroes
function removeZeros(array) {
   const no_zeroes = []
   for (const num of array) {
       num != 0 ? no_zeroes.push(num) : null
   }

   while (no_zeroes[0] > no_zeroes[1]) {
      for (let i = 0; i < no_zeroes.length ; i ++) {
         if (no_zeroes[i] > no_zeroes[i+1]) {
          let first = no_zeroes[i]
          let second = no_zeroes[i+1]
          no_zeroes[i] = second
          no_zeroes[i+1] = first
         }
     }
   }
   // and this will create a final array with zeroes sorted, without sorting the zeroes
   const final_array = []
   for (const num of array) {
      if (num == 0) {
        final_array.push(num)
      } else {
          final_array.push(no_zeroes[0])
          no_zeroes.shift()
      }
   }
return final_array
}


console.log(removeZeros(heights))