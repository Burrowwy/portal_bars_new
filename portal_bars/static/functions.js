function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("btn☰").style.opacity = "0";

}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("btn☰").style.opacity = "1";
}

function validation(form){

    function createError(input, text){
        const parent = input.parentNode;
        const errorLabel = document.createElement('label');

        errorLabel.classList.add('error-label');
        errorLabel.textContent = text;
        parent.classList.add('error');

        parent.append(errorLabel);
        console.log(parent)
    }

    function removeError(input){
        const parent = input.parentNode;

        if(parent.classList.contains('error')){
            parent.querySelector('.error-label').remove()
            parent.classList.remove('error')
        }
    }

    let result = true;

    form.querySelectorAll('input').forEach(input =>{

        removeError(input)

        if(input.dataset.name){
            const val = input.value;
            const bool = /^[А-ЯЁ][а-яё]+$/.test(val);
            if(bool === false){
                removeError(input)
                createError(input, "Неправильно задано имя");
                result = false;
            }
        }

        if(input.dataset.minLength){
            if(input.value.length < input.dataset.minLength){
                removeError(input)
                createError(input, "Минимально кол-во символов:"+input.dataset.minLength);
                result = false;
            }
        }

        if(input.dataset.maxLength){
            if(input.value.length > input.dataset.maxLength){
                removeError(input)
                createError(input, "Максимально кол-во символов:"+input.dataset.maxLength);
                result = false;
        }
        }

        if(input.value === ""){
            console.log("miss")
            removeError(input)
            createError(input, "Поле не заполнено");
            result = false;
        }
    })

    return result;
}




