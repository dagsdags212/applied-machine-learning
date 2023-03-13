module.exports = function transpose(matrix) {
    let T = [];
    let row;
    for (let r=0; r<matrix[0].length; r++) {
        row = [];
        for (let c=0; c<matrix.length; c++) {
            row.push(matrix[c][r]);
        }
        T.push(row);
    };
    return T;
};