const transpose = require('./transpose');

// house sizes
let houseSizes = [2104, 1416, 1534, 852];
let A = [];

for (let i=0; i<houseSizes.length; i++) {
    A[i] = [1, houseSizes[i]];
};

// Regression models
    // 1. h(x) = -40 + 0.25x
    // 2. h(x) = 200 + 0.1x
    // 3. h(x) = -150 + 0.4x
let B = [
    [-40, 200, -150],
    [0.25, 0.1, 0.4]
];

function multiply(A, B) {
    let product = [];
    let temp;
    let sum;
    B = transpose(B);

    for (let z=0; z<B.length; z++) {
        temp = [];
        for (let i=0; i<A.length; i++) {
            sum = 0;
            for (let j=0; j<A[i].length; j++) {
                sum += A[i][j] * B[z][j];
            }
            temp.push(sum);
        };
        product.push(temp);
    };
    return transpose(product);
};

// TEST CASES
const C = [[1,3], [2,5]];
const D = [[0,1], [3,2]];
const E = [[1,3,2], [4,0,1]];
const F = [[1,3], [0,1], [5,2]];

// console.log(multiply(A, B));
// console.log(multiply(C, D));
// console.log(multiply(E, F));