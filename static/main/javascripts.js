let nav = document.querySelector('.nav');
let span = document.getElementById('span');
let span1 = document.getElementById('span1');


span.onclick = function (){
    if (nav.style.left == '-430px'){
        nav.style.left = '-270px';
        nav.style.transition = '1.5s';
        
        
        // document.getElementById('span').style.opacity= 0
        // document.getElementById('span1').style.display = ''
        
        }else{
        nav.style.left = '-430px';
        nav.style.transition = '1.5s';
        
        
    }
}
let righte = document.querySelector('.right');
let lefte = document.querySelector('.left');
window.onscroll = function(){
    if (window.scrollY >= 540 ){
        righte.style.display = 'block'
        righte.style.opacity = '1'
        righte.style.transition = '3s'
        if(window.scrollY >= 1040){
            lefte.style.display = 'block'
            lefte.style.opacity = '1'
            lefte.style.transition = '3s'
        }else{
            lefte.style.display = 'none'
            lefte.style.opacity = '0'
            lefte.style.transition = '3.5s'
        }
    }else{
        righte.style.display = 'none'
        righte.style.opacity = '0'
        righte.style.transition = '3s'
    }

}
$('#fle').click(function(){
    $('html , body').animate({
        scrollTop : $('#fle1').offset().top
    },3000)
})
$('#fle1').click(function(){
    $('html , body').animate({
        scrollTop : $('#fle2').offset().top
    },3000)
})
$("#fle2").click(function(){
    $('html , body').animate({
        scrollTop : $('#fle3').offset().top
    },3000)
})