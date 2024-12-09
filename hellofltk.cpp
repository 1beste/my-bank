#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/fl_draw.H>
#include <vector>
#include <cstdlib>
#include <ctime>

class Pen {
public:
  Fl_Color color;
  int thickness;

  Pen(Fl_Color color, int thickness)
    : color(color)
    , thickness(thickness) {}

  virtual void drawLine(int x1, int y1, int x2, int y2) {
    fl_color(color);
    fl_line_style(FL_SOLID, thickness);
    fl_line(x1, y1, x2, y2);
    // fl_line_style(thickness);
    fl_line_style(0); // Reset line style
  }
};

class Shape {
public:
  Pen *pen;

  Shape(Pen *pen)
    : pen(pen) {}
  virtual void draw() = 0; // Pure virtual function
  virtual ~Shape() { delete pen; }
};

// Line class (subclass of Shape)
class Line : public Shape {
  int x1, y1, x2, y2;

public:
  Line(Pen *pen, int x1, int y1, int x2, int y2)
    : Shape(pen)
    , x1(x1)
    , y1(y1)
    , x2(x2)
    , y2(y2) {}

  void draw() override { pen->drawLine(x1, y1, x2, y2); }
};

// Rectangle class
class Rectangle : public Shape {
  int x, y, width, height;

public:
  Rectangle(Pen *pen, int x, int y, int width, int height)
    : Shape(pen)
    , x(x)
    , y(y)
    , width(width)
    , height(height) {}

  void draw() override {
    pen->drawLine(x, y, x + width, y);
    pen->drawLine(x + width, y, x + width, y + height);
    pen->drawLine(x + width, y + height, x, y + height);
    pen->drawLine(x, y + height, x, y);
  }
};

// Circle class
class Circle : public Shape {
  int centerX, centerY, radius;

public:
  Circle(Pen *pen, int centerX, int centerY, int radius)
    : Shape(pen)
    , centerX(centerX)
    , centerY(centerY)
    , radius(radius) {}

  void draw() override {
    fl_color(pen->color);
    fl_line_style(FL_SOLID, pen->thickness);
    fl_circle(centerX, centerY, radius);
    fl_line_style(0); // Reset line style
  }
};

class Canvas : public Fl_Widget {
  std::vector<Shape *> shapes; // Tüm şekilleri saklayan vektör
public:
  Canvas(int X, int Y, int W, int H)
    : Fl_Widget(X, Y, W, H) {}

  void addShape(Shape *shape) {
    shapes.push_back(shape); // Yeni şekli ekle
    redraw();                // Tüm şekilleri yeniden çiz
  }

  void clear() {
    for (auto shape : shapes) {
      delete shape; // Belleği temizle
    }
    shapes.clear();
    redraw(); // Ekranı temizle
  }

  void draw() override {
    fl_color(FL_WHITE);           // Arka plan rengini beyaz yap
    fl_rectf(x(), y(), w(), h()); // Arka planı doldur

    for (auto shape : shapes) { // Tüm şekilleri çiz
      shape->draw();
    }
  }

  ~Canvas() { clear(); }
};


// Function to generate a random color
Fl_Color randomColor() {
  return fl_rgb_color(rand() % 256, rand() % 256, rand() % 256);
}

// Function to generate a random thickness
int randomThickness() {
  return rand() % 4 + 1; // Thickness between 1 and 4
}


// Function to draw a random line with unique color and thickness
void drawRandomLine(Fl_Widget *, void *data) {
  Canvas *canvas = (Canvas *)data;

  int x1 = canvas->x() + rand() % canvas->w();
  int y1 = canvas->y() + rand() % canvas->h();
  int x2 = canvas->x() + rand() % canvas->w();
  int y2 = canvas->y() + rand() % canvas->h();

  Pen *pen = new Pen(randomColor(), randomThickness());
  Line *line = new Line(pen, x1, y1, x2, y2);
  canvas->addShape(line);
}

// Function to draw a random rectangle with unique color and thickness
void drawRandomRectangle(Fl_Widget *, void *data) {
  Canvas *canvas = (Canvas *)data;

  int width = rand() % 100 + 20;
  int height = rand() % 100 + 20;
  int x = canvas->x() + rand() % (canvas->w() - width);
  int y = canvas->y() + rand() % (canvas->h() - height);

  Pen *pen = new Pen(randomColor(), randomThickness());
  Rectangle *rect = new Rectangle(pen, x, y, width, height);
  canvas->addShape(rect);
}

// Function to draw a random circle with unique color and thickness
void drawRandomCircle(Fl_Widget *, void *data) {
  Canvas *canvas = (Canvas *)data;

  int radius = rand() % 50 + 10;
  int x = canvas->x() + radius + rand() % (canvas->w() - 2 * radius);
  int y = canvas->y() + radius + rand() % (canvas->h() - 2 * radius);

  Pen *pen = new Pen(randomColor(), randomThickness());
  Circle *circle = new Circle(pen, x, y, radius);
  canvas->addShape(circle);
}


// Function to clear the canvas
void clearCanvas(Fl_Widget *, void *data) {
  Canvas *canvas = (Canvas *)data;
  canvas->clear();
}

int main() {
  srand(time(0));

  Fl_Window *window = new Fl_Window(1280, 720, "Shape Drawer");

  Canvas *canvas = new Canvas(10, 50, 1260, 660);

  Fl_Button *lineButton = new Fl_Button(10, 10, 100, 30, "Draw Line");
  lineButton->callback(drawRandomLine, canvas);

  Fl_Button *rectButton = new Fl_Button(120, 10, 100, 30, "Draw Rectangle");
  rectButton->callback(drawRandomRectangle, canvas);

  Fl_Button *circleButton = new Fl_Button(230, 10, 100, 30, "Draw Circle");
  circleButton->callback(drawRandomCircle, canvas);

  Fl_Button *clearButton = new Fl_Button(340, 10, 100, 30, "Clear");
  clearButton->callback(clearCanvas, canvas);

  window->end();
  window->show();

  return Fl::run();
}