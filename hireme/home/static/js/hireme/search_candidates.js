$( function() {

     var availableTags = JSON.parse(document.getElementById("all_roles").value);

    $( "#search_textbox" ).autocomplete({
      source: availableTags
    });
  } );



new Vue({
	el: '#hrsection',
	data() {
  	return {
    	loading: true,
      recent_candidates: [],
      search_keyword:''
    }
  },
    methods: {
    SearchResume: function(e) {
      if (e.keyCode === 13) {
          this.search_keyword = $('#search_textbox').val()

          axios.post("/employer/search_with_keyword", {
                search_keyword: $('#search_textbox').val()
                })
                .then(response => {
                    this.recent_candidates = response.data.recent_candidates
                    console.log(this.recent_candidates)
                    $('#search_textbox').val(this.search_keyword)
                })
                .catch(e => {
                console.log(e)
                })

      }
    },

},
  created() {
          	axios.get("/load_recent_candidates").then((response) => {
                setTimeout(() => this.recent_candidates = response.data.recent_candidates, 500);
                setTimeout(() => this.loading = false, 500);
    })

  }
})