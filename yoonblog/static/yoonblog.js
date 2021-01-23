let menu_status = false;
function turn_menu(){
if(menu_status == false){
    menu_status = true;
} else {
    menu_status = false;
}
menu_flipper();
}
function menu_flipper(){
    const menuScreen = document.getElementById('menu');
    const pageScreen = document.getElementById('full');
    if(menu_status == true){
        menuScreen.style.width = '400px';
        menuScreen.style.padding = '0px 12px 30px';
        pageScreen.style.marginRight = '0';
        document.getElementById('menu-open').style.display = 'none';
        document.getElementById('menu-fold').style.display = 'block';
    } else {
        menuScreen.style = menuScreen.defaultValue;
        pageScreen.style = pageScreen.defaultValue;
        document.getElementById('menu-open').style.display = 'block';
        document.getElementById('menu-fold').style.display = 'none';
    }
}

function pageDown(){
    const full = document.getElementById('full')
    full.scrollTo(0,1000)
}
function pageDownSmooth(){
    const full = document.getElementById('full')
    full.scrollTo({
        top: 1000,
        behavior: 'smooth'
      });
}