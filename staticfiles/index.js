
   let toggle= document.querySelectorAll('.toggle');
   let buttons= document.querySelectorAll('.buttons');
   toggler();
   
   

   function displayElement(e){
     toggler();
      let id = e.name;
      document.getElementById(`${id}`).style.display="block";
   }
function toggler(){
       toggle.forEach(e=>{
        e.style.display="none";
    })
}
