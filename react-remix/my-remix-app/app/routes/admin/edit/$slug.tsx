import { useRef } from "react"
import { Form, ActionFunction, redirect, useActionData, useTransition, LoaderFunction, useLoaderData } from "remix"
import invariant from "tiny-invariant"
import { editPost, getPost } from "~/post"

interface PostError {
  title?: boolean,
  slug?: boolean,
  markdown?: boolean
}

export const loader: LoaderFunction = async ({ params }) => {
  invariant(params.slug, 'Expected params.slug')
  return getPost(params.slug, true)
}

export const action: ActionFunction = async ({ request }) => {
  await new Promise(res => setTimeout(res, 1000))

  const formData = await request.formData()

  const title = formData.get("title")
  const slug = formData.get("slug")
  const markdown = formData.get("markdown")
  const oldSlug = formData.get("old_slug")

  const errors: PostError = {}
  if (!title) errors.title = true;
  if (!slug) errors.slug = true;
  if (!markdown) errors.markdown = true;

  if (Object.keys(errors).length) {
    return errors;
  }

  invariant(typeof title === "string")
  invariant(typeof slug === "string")
  invariant(typeof markdown === "string")
  invariant(typeof oldSlug === "string")


  await editPost({ title, slug, markdown, oldSlug })

  return redirect("/admin")

}

export default function EditPost() {

  const errors = useActionData()
  const transition = useTransition()
  const post = useLoaderData()
  debugger

  const title = useRef(post.title)
  const slug = useRef(post.slug)
  const markdown = useRef(post.markdown)


  return (
    <Form method="post">
      <p>
        <label>
          Post Title:{" "}
          {errors?.title ? (
            <em>Title is required</em>
          ) : null}
          <input defaultValue={post.title} type="text" name="title" ref={title} />
        </label>
      </p>
      <p>
        <label>
          Post Slug:{" "}
          {errors?.slug ? <em>Slug is required</em> : null}
          <input defaultValue={post.slug} type="text" name="slug" ref={slug} />
        </label>
      </p>
      <p>
        <label htmlFor="markdown">Markdown:</label>{" "}
        {errors?.markdown ? (
          <em>Markdown is required</em>
        ) : null}
        <br />
        <textarea defaultValue={post.markdown} rows={20} ref={markdown} name="markdown" />
      </p>
      <p>
        <button type="submit">{
          transition.submission
            ? 'Creating...'
            : 'Create Post'
        }</button>
      </p>
      <input type="hidden" name="old_slug" value={post.slug} />
    </Form>
  )
}