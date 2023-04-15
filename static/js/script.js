question_num=document.getElementById("question_num");
question=document.getElementById("question");
flexRadioDefault1=document.getElementById("flexRadioDefault1");
flexRadioDefault2=document.getElementById("flexRadioDefault2");
flexRadioDefault3=document.getElementById("flexRadioDefault3");
flexRadioDefault4=document.getElementById("flexRadioDefault4");
option1=document.getElementById("option1");
option2=document.getElementById("option2");
option3=document.getElementById("option3");
option4=document.getElementById("option4");


let score=0;
let clickcount=1;
document.querySelectorAll(".btn")[1].addEventListener("click", () => {
    
    clickcount++;
    if(clickcount==2)
    {
        question_num.innerHTML="Question 2";
        question.innerHTML="Which state produces maximum soybean?";
        option1.innerHTML="Madhya Pradesh";
        option2.innerHTML="Uttar Pradesh";
        option3.innerHTML="Bihar";
        option4.innerHTML="Rajasthan";
        if(flexRadioDefault4.checked)
        {
            score=score+10;
            alert("correct");
        }
        else
        {
            alert("incorrect");
        }
    }
    else if(clickcount==3){
        question_num.innerHTML="Question 3";
        question.innerHTML="Which country operationalized world’s largest radio telescope?";
        option1.innerHTML="USA";
        option2.innerHTML="China";
        option3.innerHTML="Russia";
        option4.innerHTML="India";
        if(flexRadioDefault1.checked)
        {
            score=score+10;
            alert("correct");
        }
        else
        {
            alert("incorrect");
        }
        
    }
    else if(clickcount==4){
        question_num.innerHTML="Question 4";
        question.innerHTML="Which of the following is the capital of Arunachal Pradesh?";
        option1.innerHTML="Itanagar";
        option2.innerHTML="Dispur";
        option3.innerHTML="Imphal";
        option4.innerHTML="Panaji";
        if(flexRadioDefault2.checked)
        {
            score=score+10;
            alert("correct");
        }
        else
        alert("incorrect");
    }
    else if(clickcount==5){
        question_num.innerHTML="Question 5";
        question.innerHTML="Which one among the following radiations carries maximum energy?";
        option1.innerHTML="Ultraviolet rays";
        option2.innerHTML="Gamma rays";
        option3.innerHTML="X-rays";
        option4.innerHTML="Infra-red rays";
        
        if(flexRadioDefault1.checked)
        {
            score=score+10;
            alert("correct");
        }
        else
        alert("incorrect");
    }
    else
    {
        
        if(flexRadioDefault2.checked)
        {
            score=score+10;
            alert("correct");
        }
        else
        alert("incorrect");
        window.location.replace("/thankyou/"+score+"");
    }
});
