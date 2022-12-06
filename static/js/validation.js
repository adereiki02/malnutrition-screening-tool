function subme() {
    var inputs = document.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i +=1) {
        if (inputs[i].value == '') {
            alert ("tidak boleh ksosong")
            exit()
        }
    }
    document.getElementById("myForm").submit()
}