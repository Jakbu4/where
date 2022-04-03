let inputfield = document.querySelector(".localisation_text_field");
let box = document.querySelector(".autofill_bg");
let sugg_field = document.querySelector(".autofii_ul");


inputfield.onkeyup = (e)=>{
    let useroutput = e.target.value;
    let arr = [];
    if(useroutput){
        arr = sugg.filter((data)=>{
            return data.toLocaleLowerCase().startsWith(useroutput.toLocaleLowerCase());
        }).slice(0,5);
        arr = arr.map((data)=>{
            return data = "<li class='autofill_li'>" + data + "</li>";
        });
        box.classList.add("active");
        showList(arr);
        let suggestList = sugg_field.querySelectorAll("li");
        for( let i = 0; i<suggestList.length; i++){
            suggestList[i].setAttribute("onclick", "fill(this)");
        }
    }else{
        box.classList.remove("active");
    }
    
}

function fill(el){
    let choose = el.textContent;
    inputfield.value = choose;
    box.classList.remove("active");
}

function showList(list){
    let sugglist;
    if(!list.length){
        a = inputfield.value;
        sugglist = "<li class='autofill_li'>" + a + "</li>";
    }else{
        sugglist = list.join("");
    }
    sugg_field.innerHTML = sugglist;
}