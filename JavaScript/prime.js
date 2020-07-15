let listPrime = [];

function isPrime(numberToVerify){
    if(numberToVerify == 1){return false};
    if(numberToVerify <= 3){return true};
    if((numberToVerify % 2) == 0){return false};
    for(a = 3; a <= Math.floor(Math.sqrt(numberToVerify)); a += 2){
        if((numberToVerify % a) == 0){return false};
    };
    return true;
}

for(i = 1; i < 1000; i++){
    if(isPrime(i)){
        listPrime.push(i);
    };
}

console.log(listPrime);
