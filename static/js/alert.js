function submitForm(form) {
    swal ({
      title: "Apakah Anda yakin?",
      text: "Data tidak dapat diubah setelah dikirim",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((isOkay) => {
      if(isOkay) {
        form.submit();
      }
    });
    return false;
  } 
