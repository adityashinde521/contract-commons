import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const lessons = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/lessons' }),
  schema: z.object({
    title: z.string(),
    module: z.number(),
    order: z.number(),
    kind: z.enum(['lesson', 'lab-remix', 'lab-gui', 'reading']),
    minutes: z.string().optional(),
    legacy: z.string().optional(),
    problem: z.string(),
  }),
});

const pages = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/pages' }),
  schema: z.object({ title: z.string(), minutes: z.string().optional() }),
});

export const collections = { lessons, pages };
