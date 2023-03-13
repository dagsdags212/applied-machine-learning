let A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
];

let B = [
    [3,4,9],
    [1,5,18],
    [9,1,6]
];

function add(A, B) {
    if (A.length !== B.length) {
        console.log('Cannot add two vectors of different dimensions');
        return null;
    }
    let sum = [];
    let row;
    for (let r=0; r<A.length; r++) {
        row = [];
        for (let c=0; c<A[r].length; c++) {
            row.push(A[r][c] + B[r][c]);
        }
        sum.push(row);
    }
    return sum;
}

console.log(add(A, B));