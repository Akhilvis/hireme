
var app = new Vue({
  el: '#upload_resume',
  data: {
    title: 'vue-simple-upload'
  },
  components: {
    'fileupload': FileUpload.FileUpload
  }
})


var app = new Vue({
  el: '#ftco-nav',
  data: {},
  methods: {
    scroll: function(div_id) {
             $('html, body').animate({
                scrollTop: $(div_id).offset().top
            }, 1000);
            $('#ftco-nav').removeClass('show');
        }
        }
})



new Vue({
    el: '#cand_form',

    data: {
        name: '',
        email: '',
        mobile: '',
        role: '',
        experience: '',
        summary:'',
    },

    methods: {
        search: function(e) {
            e.preventDefault();

            $.post("/employee/add_candidate_data", {
                "name": this.name,
                "email": this.email,
                "mobile": this.mobile,
                "role": this.role,
                "experience": this.experience,
                "summary": this.summary

                }, function(result){
                console.log(result.status == 0)
                if(result.status == 0){
                    $('#resume_success').text('Please upload resume first !')
                    $('#resume_success').addClass("alert-danger");
                }
                else if(result.status == 1){
                    $('#resume_success').text('Candidate registered successfully !')
                    $('#resume_success').addClass("alert-success");

                }
                $('#resume_success').show()
                this.name = ''
              });

        }
    }
});

$(document).ready(function(){
    $('#resume_success').hide()
});
