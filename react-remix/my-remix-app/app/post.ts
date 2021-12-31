import path from 'path'
import fs from 'fs/promises'
import parseFrontMatter from 'front-matter'
import invariant from 'tiny-invariant'
import { marked } from 'marked'

export interface Post {
  slug: string,
  title: string
}

export interface NewPost extends Post {
  markdown: string
}

export interface EditPost extends NewPost {
  oldSlug: string
}

export interface PostMarkdownAttributes {
  title: string
}

function isValidPostAttributes(attributes: any): attributes is PostMarkdownAttributes {
  return attributes?.title
}

const postsPath = path.join(__dirname, "..", "posts")

export async function getPosts() {
  const dir = await fs.readdir(postsPath)
  return Promise.all(
    dir.map(async filename => {
      const file = await fs.readFile(path.join(postsPath, filename))
      const { attributes } = parseFrontMatter(file.toString())
      invariant(
        isValidPostAttributes(attributes),
        `${filename} has bad data!`
      )
      return {
        slug: filename.replace(/\.md$/, ""),
        title: attributes.title
      }
    })
  )
}

export async function getPost(slug: string, withOriginalMarkup: boolean = false) {
  const filepath = path.join(postsPath, slug + ".md");
  const file = await fs.readFile(filepath);
  const { attributes, body } = parseFrontMatter(file.toString());
  invariant(
    isValidPostAttributes(attributes),
    `Post ${filepath} is missing attributes`
  );
  if (withOriginalMarkup) {
    return { slug, markdown: body, title: attributes.title };
  } else {
    const html = marked(body)
    return { slug, html, title: attributes.title };
  }
}

export async function createPost(post: NewPost) {
  const md = `---\ntitle: ${post.title}\n---\n\n${post.markdown}`

  await fs.writeFile(
    path.join(postsPath, post.slug + ".md"),
    md
  )

  return getPost(post.slug)
}

export async function editPost(post: EditPost) {
  const { slug, title, markdown, oldSlug } = post

  if (slug !== oldSlug) {
    await fs.unlink(
      path.join(postsPath, oldSlug + ".md"),
    )
  }

  return createPost({ slug, title, markdown })
}

