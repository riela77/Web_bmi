// 유효성 검사 모음집
//다양한 상황에 대응가능하게 최대한 일반적으로 
//----------------------------------------

//글자 써져있는지/파일이 들어있는지 확인
function isEmpty(field){
    return !field.value;
}
// len최소글자수 보다 짧으면 true, 길면 false
function lessThan(field,len){
    // alert("ㅎ");
    // 긴지 아닌지자체가 false,true로 나오니까
    return field.value.length<len;
}
// input글자에 한글,한자,일본어가 들어있으면 안되고
//  영어숫자 특수문자로만 구성되어있으면 false가 뜨게
function containHS(field) {
    // 영어 대소문자와 숫자 특수문자만 허용
    var pattern = /^[A-Za-z0-9!@#$%^&*()\-_+=~`[\]{}|\\;:'",.<>/?]*$/;
    return !pattern.test(field.value);
}
function isNotOnlyKorean(field) {
    var pattern = /^[가-힣]+$/;
    return !pattern.test(field.value);  // 이건 "한글이 아니면 true"
}



// pw랑 pw확인이랑 내용이 같은지 다른지
function notEqual(field1,field2){
    return field1.value!=field2.value;
}
// 문자열 세트를 넣었을때 그게 안들어있으면 true가 출력되서 check 실행 안되게 하는 함수
function notConstains(field,set){
    for(var i=0;i<set.length;i++){
        if(field.value.indexOf(set[i]) !=-1){
            return false;
        }
    }return true;
}
// input에 숫자가 아닌거 넣거나 띄어쓰기 있으면 true.
function isNotNum(field){
    return isNaN(Number(field.value)) || (field.value.indexOf(" ") != -1);
}


// 사용자프로필 사진 올리기 

// 프로필 사진파일 형식 맞추기
//파일타입에서 field.value하면 선택한 파일명이 글자로 주어짐. 
// type에 해당하는 파일 양식만 업로드 가능하게
function isNotType(field, type){
    // 파일 이름을 다 소문자로 바꿔서 png가 있나 없나
    var filename = field.value.toLowerCase();
    return filename.endsWith("." + type);
}
