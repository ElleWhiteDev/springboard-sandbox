$(".delete-todo").click(deleteTodo)
    
async function deleteTodo() {
    const id = $(this).data('id')
    await axios.delete(`/api/todos/${id}`)  //backtics ` for f string
    $(this).parent().remove()
}
