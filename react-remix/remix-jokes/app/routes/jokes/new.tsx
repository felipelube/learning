import React from "react"

export default function NewJokeRoute({ }) {
  return (
    <div>
      <form>
        <div>
          <label htmlFor="name">Name</label>
        </div>
        <div>
          <input type="text" name="name" />
        </div>

        <div>
          <label htmlFor="content">Content</label>
        </div>
        <div>
          <textarea name="content" id="content"></textarea>
        </div>
        <div><button type="submit">OK</button></div>
      </form>
    </div>
  )
}