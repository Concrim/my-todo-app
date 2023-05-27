import streamlit as st
import functions

todo_list = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todo_list.append(todo+'\n')
    functions.write_todos(todo_list)
    st.session_state["new_todo"] = ' '


st.title("To-do List")
st.subheader("This is your very own to-do list.")
st.write("Write something, baka.")

for todo_local in todo_list:
    check = st.checkbox(todo_local, key=todo_local)
    if check:
        todo_list.remove(todo_local)
        functions.write_todos(todo_list)
        del st.session_state[todo_local]
        st.experimental_rerun()

st.text_input(label="Enter a todo here: ",
              placeholder="Type here.",
              on_change=add_todo,
              key='new_todo')
