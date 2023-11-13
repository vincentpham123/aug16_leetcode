const pairedParentheses1 = (str) => {
    // i can keep track of one parenthesis, and then check if the other side occurs after
    // if so I can return true 
    const hash ={'(':[], ')':[]}
    for(let i =0; i< str.length;i++){
      let char = str[i]
      if(hash[char]){
        hash[char].push(i);
      }
    }
    first= Object.values(hash)[0];
    second = Object.values(hash)[1];
    if (first.length !== second.length) return false;
    for (let i =0; i < first.length;i++){
      if (first[i]>second[i]) return false;
    }
    return true;
  };

const pairedParentheses = (str) => {
    let count =0;
    // i know each parenthesis will cancel each other out
    // as iterate through, I can check for both
    // depending on which one, i can increment or decrement my count
    
    for (let char of str){
      if(char ==='('){
        count +=1
      } else if (char===')') {
        if (count ===0) return false;
        count -=1
      }
    }
    return count ===0
  };
  