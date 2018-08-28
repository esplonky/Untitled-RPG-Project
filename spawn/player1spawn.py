var mousex;
var mousey;
var mouseSeedX;
var mouseSeedY;
var seedX;
var seedY;

mousey = window_mouse_get_y();
mousex = window_mouse_get_x();



mouseSeedX = mousey + mousex;
mouseSeedY = mouseSeedX / 2;

seedX = random_set_seed(mouseSeedX);
seedY = random_set_seed(mouseSeedY);

player0.x = seedX;
player0.y = seedY;




