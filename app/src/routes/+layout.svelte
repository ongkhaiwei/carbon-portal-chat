<script>
    import { browser } from "$app/environment";
    import { theme } from "$lib/stores";
    import "carbon-components-svelte/css/all.css";
    import { Loading, Header, HeaderNav, HeaderNavItem, HeaderGlobalAction, HeaderUtilities, SideNav, SideNavItems, SideNavMenu, SideNavMenuItem, SideNavLink, SideNavDivider, SkipToContent, Content, Grid, Row, Column } from "carbon-components-svelte";
    import { page } from "$app/stores";
    import { onMount } from "svelte";
    import TextLinkAnalysis from "carbon-icons-svelte/lib/TextLinkAnalysis.svelte";
    import Asleep from "carbon-icons-svelte/lib/Asleep.svelte";
    import AsleepFilled from "carbon-icons-svelte/lib/AsleepFilled.svelte";

    let isSideNavOpen = true;
    
    $: {
      if (browser) {
        document.documentElement.setAttribute("theme", $theme);
      }
    }
    const toggleTheme = () => {
      $theme = $theme === "white" ? "g100" : "white";
    };
    onMount(() => {

    });
  </script>
  
  <svelte:head>
    <title>Carbon Portal | IBM</title>
    <link rel="icon" href="https://svelte.carbondesignsystem.com/favicon.ico" type="image/x-icon">
  </svelte:head>
  
  <Header company="IBM" platformName=" | Carbon Portal" bind:isSideNavOpen>
    <svelte:fragment slot="skip-to-content">
      <SkipToContent />
    </svelte:fragment>
    <HeaderNav>
      <HeaderNavItem href="#" text="Services" />
      <HeaderNavItem href="#" text="Explore" />
      <HeaderNavItem href="#" text="Support" />
    </HeaderNav>
    <HeaderUtilities>
      <HeaderGlobalAction on:click={toggleTheme} icon={$theme === "white" ? AsleepFilled : Asleep} />
    </HeaderUtilities>
  </Header>
  
  <SideNav bind:isOpen={isSideNavOpen} rail>
    <SideNavItems>
      <SideNavLink icon={TextLinkAnalysis} text="Home" href="/" isSelected={$page.url.pathname == "/"} />
    </SideNavItems>
  </SideNav>
  
  <Content>
    {#if browser}
      <slot />
    {:else}
      <Loading />
    {/if}
  </Content>