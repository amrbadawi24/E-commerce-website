let scrol=document.getElementById('scrol');
scrol.onclick=function(){
    window.scrollTo({
        left:0,
        top:0,
        behavior:"smooth"
    });
};