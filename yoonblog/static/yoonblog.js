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
    if(menu_status == true){
        menuScreen.style.width = '400px';
        menuScreen.style.padding = '0px 12px 30px';
        document.getElementById('menu-open').style.display = 'none';
        document.getElementById('menu-fold').style.display = 'block';
    } else {
        menuScreen.style.width = '0%';
        menuScreen.style.padding = '0 0 30px';
        document.getElementById('menu-open').style.display = 'block';
        document.getElementById('menu-fold').style.display = 'none';
    }
}
// function page_down(){
//     if
// }