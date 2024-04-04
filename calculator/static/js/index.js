const baseUrl = 'http://127.0.0.1:8000/';
const add = 'add/';
const subtract = 'subtract/';
const multiply = 'multiply/';
const divide = 'divide/';

let errorsArray = ['ZeroDivisionError'];
let currentInput = '';
let symbolsArr = ['+', '-', '*', '/', '.', '%'];

function getDisplay() {
    return document.getElementById('display');
}

function appendSymbol(num) {
    let display = getDisplay();
    if (currentInput === '0' && symbolsArr.includes(num)) {
        alert('Used invalid format');
    } else if (symbolsArr.includes(currentInput[currentInput.length - 1]) && symbolsArr.includes(num)) {
        currentInput = currentInput.slice(0, -1) + num;
        display.innerText = currentInput;
    } else {
        if (currentInput === '0' || errorsArray.includes(currentInput)) {
            currentInput = '';
        }
        if (num === '%') {
            currentInput = (parseFloat(currentInput) / 100).toString();
            display.innerText = currentInput;
        } else {
            currentInput += num;
            display.innerText = currentInput;
            display.style.fontSize = '48px';
        }
    }
}

function clearDisplay() {
    let display = getDisplay();
    currentInput = '0';
    display.innerText = currentInput;
    display.style.fontSize = '48px';
}

function changeSign() {
    let display = getDisplay();

    if (currentInput !== '0' && !isNaN(currentInput)) {
        currentInput = (-parseFloat(currentInput)).toString();
        display.innerText = currentInput;
    }
}

$(document).ready(function () {
    $.get(baseUrl)
        .done(function (resp) {
        })
        .fail(function (resp) {
        });

    $('#equal').submit(function (event) {
event.preventDefault();
let display = $('#display').text();
if (display !== '0') {
    let parts = display.split(/([\+\-\*\/])/).map(part => part.trim());
    parts = parts.filter(part => part !== '');
    if (parts.length === 3) {
        let operands = [parts[0], parts[2]];
        let operator = parts[1];

        let dataForm = JSON.stringify({
            "a": parseFloat(operands[0]),
            "b": parseFloat(operands[1])
        });
        let url;
        switch (operator) {
            case '+':
                url = baseUrl + add;
                break;
            case '-':
                url = baseUrl + subtract;
                break;
            case '*':
                url = baseUrl + multiply;
                break;
            case '/':
                url = baseUrl + divide;
                break;
            default:
                break;
        }
        if (url) {
            upload(url, dataForm);
        } else {
            $(this).prop('disabled', true);
        }
    } else {
        $(this).prop('disabled', true);
    }
} else {
    $(this).prop('disabled', true);
}

        function upload(urlSet, dataSet) {
            $.ajaxSetup({
                headers: {
                    'X-CSRFToken': $('[name="csrfmiddlewaretoken"]').val()
                }
            });

            $.post({
                url: urlSet,
                data: dataSet,
                contentType: 'application/json',
                success: function (response) {
                    console.log(response);
                    let display = getDisplay();
                    if (response.status === 'ok') {
                        display.textContent = response.result;
                        currentInput = '0';
                    } else {
                        display.style.fontSize = '30px';
                        display.textContent = response.message;
                        currentInput = '0';
                    }

                },
                error: function (response) {
                    console.log(response);
                }
            })
        }
    });
});
