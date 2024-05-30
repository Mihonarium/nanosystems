// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Nanosystems',
  tagline: 'Eric Drexler',
	
  url: 'https://nanosyste.ms',
  baseUrl: '/',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: 'sidebars.js',
          routeBasePath: '/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],
	stylesheets: [
	  {
		href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
		type: 'text/css',
		integrity:
		  'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
		crossorigin: 'anonymous',
	  },
	],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      //image: 'img/docusaurus-social-card.jpg',
      navbar: {
		hideOnScroll: true,
        title: 'Eric Drexler - Nanosystems',
      },
      footer: {
        style: 'dark',
        links: [],
        copyright: `Book by K. Eric Drexler. Copyright (C) 1992 by John Wiley & Sons, Inc. John Wiley & Sons, Inc. retains the rights to the book in print.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
		algolia: {
		  // The application ID provided by Algolia
		  appId: 'Z72L4M9T7U',
		  // Public API key: it is safe to commit it
		  apiKey: '5c1cabebb542a4a41fcaaf9ee93e22cd',
		  indexName: 'nanosyste',
		  contextualSearch: true,
		  //searchParameters: {},
		  searchPagePath: false,

		  // Optional: whether the insights feature is enabled or not on Docsearch (`false` by default)
		  insights: false,
		},
    }),
	  scripts: [
	  {
	  	src: 'https://nanosyste.ms/js/remember_scroll.js',
		async: true,
	  },
  ],
};

export default config;
