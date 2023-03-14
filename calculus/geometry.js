// The Essence of Calculus by 3Blue1Brown

// Episode 1: Introduction 
class Circle {
    constructor(r) {
        this.r = r;
        this.area = Math.PI * r * r;
        this.circumference = 2 * Math.PI * r;
    }

    getArea() {
        return this.area;
    }

    approximateArea(dr = 0.01) {
        let area = 0;
        let radius;
        for (let R=0; R<this.r; R += dr) {
            radius = R * dr;
            area += 2 * Math.PI * radius;
        };
        return area;
    }

    getCircumference() {
        return this.circumference;
    }
}

let circle = new Circle(3);
// console.log(circle.getArea());
// console.log(circle.getCircumference());

// the area of the circle gets closer to the true value as dt decreases
// console.log(circle.approximateArea(1));
// console.log(circle.approximateArea(0.1));
// console.log(circle.approximateArea(0.01));
// console.log(circle.approximateArea(0.001));
// console.log(circle.approximateArea(0.0001));
// console.log(circle.getArea());

// Episode 2: The Paradox of the Derivative
class Speed {
    constructor(distance, time) {
        this.distance = distance;
        this.time = time;
    }

    calculateSpeed() {
        return this.distance / this.time;
    }

    calculateVelocity(dt) {
        let vel = 0;
        for (let T=0; T<this.time; T += dt) {
            vel += (this.distance * (this.time + dt) - (this.distance * this.time)) / (dt);
        }
        return vel;
    }
};

let car = new Speed(50, 5);
console.log(car.calculateSpeed());
