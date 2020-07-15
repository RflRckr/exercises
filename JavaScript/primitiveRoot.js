let results = [];
function isPrime(numberToVerify){
    if(numberToVerify == 1){return false};
    if(numberToVerify <= 3){return true};
    if((numberToVerify % 2) == 0){return false};
    for(a = 3; a <= Math.floor(Math.sqrt(numberToVerify)); a += 2){
        if((numberToVerify % a) == 0){return false};
    };
    return true;
}

function findPrimitiveRoot(prime){
    let numberList  = [], rootsList = [];
    if(isPrime(prime)){
        maxnumber = prime - 1;
        for(possibleRoot = 2; possibleRoot < prime; possibleRoot++){
            for(j = 0; j < maxnumber; j++){
                var x = Math.pow(possibleRoot, j) % prime;
                numberList.push(x);
            }
            numberList.sort((a, b) => a - b);
            //console.log(numberList);
            let counter = 0;

            for(i = 0; i < numberList.length; i++){
                counter = counter + parseInt(numberList[i]);
            };
            let sum = prime*(prime + 1)/2;
            console.log(counter);
            if(counter == sum){rootsList.push(possibleRoot)};
            numberList = [];
        }    
    }
    console.log(rootsList);
}

findPrimitiveRoot(229);
