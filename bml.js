function calculateBMI(){
    var nameField=document.bmiform.name
    var heightField=document.bmiform.height
    var weightField=document.bmiform.weight
    var psaField=document.bmiform.psa
    //셋중 하나만 
    if(isEmpty(nameField)||isNotOnlyKorean(nameField)){
        alert("name?");
        nameField.value="";
        nameField.focus();
        return false;}
    if(isEmpty(heightField)||lessThan(heightField,1)||isNotNum(heightField)){
        alert("height?");
        heightField.value="";
        heightField.focus();
        return false;}
    if(isEmpty(weightField)||isNotNum(weightField)){
        alert("weight?");
        weightField.value="";
        weightField.focus();
        return false;}

    if(isEmpty(psaField)||isNotType(psaField,png)){
        alert("psa?");
        psaField.value="";
        psaField.focus();
        return false;}

    return true;
}