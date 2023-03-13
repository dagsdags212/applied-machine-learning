let A = [
    [3,4,9],
    [1,5,18],
    [9,1,6]
];
let B = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
];

function subtract(A, B) {
    if (A.length !== B.length) {
        console.log('Cannot subtract two vectors of different dimensions');
        return null;
    }
    let diff = [];
    let row;
    for (let r=0; r<A.length; r++) {
        row = [];
        for (let c=0; c<A[r].length; c++) {
            row.push(A[r][c] - B[r][c]);
        }
        diff.push(row);
    }
    return diff;
}

// console.log(subtract(A, B));