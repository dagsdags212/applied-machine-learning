// computes for the determinant of a square matrix
function determinant(m) {
    if (m.length == 1) {
        return  m[0][0];
    } else if (m.length == 2) {
        return m[0][0]*m[1][1]-m[0][1]*m[1][0];
    }

    return m[0].reduce((r,e,i) => 
        r + (-1) ** (i+2) * e * determinant(m.slice(1).map(c => 
        c.filter((_, j) => i != j))), 0);
};

const test1 = [[3]]                      // 3
const test2 = [[3,-2],[7,4]]             // 26
const test3 = [[1,3,7],[2,-1,4],[5,0,2]] // 81

console.log(determinant(test1));
console.log(determinant(test2));
console.log(determinant(test3));