let ang = 332
function setup() {
  createCanvas(800, 800)
  angleMode(DEGREES)
  noFill()
}

function draw() {
  strokeWeight(6)
  fill(30,133,78)
  square(100,100, 600, 105)
  fill('white')
  circle(400, 400, 280)
  strokeWeight(3)
  textFont('Monoton')
  textSize(60)
  textAlign(CENTER)
  text('Class of 2025', 400, 205)
  textFont('Montserrat')
  textSize(25)
  textWrap(WORD)
  textAlign(CENTER)
  text('In intellectual pursuit, we shall reflect discipline and passion for learning.',160, 575, 500, 300)
  translate(width / 2, height / 2)
  rotate(ang)
  fill('black')
  circle(0, 0, 40)
  for (let i = 0; i < 3; i++) {
    noFill();
    ellipse(0, 0, 80, 240)
    rotate(120)
  }
  for (let i = 0; i < 3; i++) {
    fill('black')
    circle(40 * cos(ang*5), 120 * sin(ang*5), 20)
    rotate(120)
  }
  ang += 1.4
}

function drawText(font) {
  fill('#ED225D');
  textFont(font, 36);
  text('p5*js', 10, 50);
}
