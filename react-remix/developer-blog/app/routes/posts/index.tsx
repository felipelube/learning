import { Link } from "remix"
import { useLoaderData } from "remix"
import { Post, getPosts } from "~/post"

export const loader = () => {
  return getPosts()
}


export default function Posts() {
  const posts = useLoaderData<Post[]>()
  console.log(posts)
  return (
    <div>
      <h1>Posts</h1>
      {Array.isArray(posts) && <ul>{posts.map(post => <li key={post.slug}><Link to={post.slug}>{post.title}</Link> </li>)}</ul>}
    </div>
  )
}