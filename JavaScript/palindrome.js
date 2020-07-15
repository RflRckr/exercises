function palindrome(str) {
    let strArray = [], reverseStrArray = [];
  let reverseStr;
  const relevantChar = /[0-9a-zA-Z]/

  //Separate only the letters and numbers into two arrays
  for(var i = 0; i < str.length; i++){
      if(str.charAt(i).match(relevantChar) != null){
          strArray.push(str.charAt(i));
          reverseStrArray.push(str.charAt(i));
      }
  }

  //transform array to string
  str = strArray.join('').toLowerCase();

  //reverse the array and transform into string
  reverseStr = reverseStrArray.reverse().join('').toLowerCase();

  //Compare the two strings
  if(str === reverseStr){
      return true;
  } else {
      return false;
  }
}
  console.log(palindrome("A man, a plan, a canal. Panama"));
  console.log(palindrome("My age is 0, 0 si ega ym."))
  console.log(palindrome("0_0 (: /-\ :) 0-0"));
