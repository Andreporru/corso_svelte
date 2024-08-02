<script lang="ts">
	interface Props {
		direction?: 'row' | 'column';
		nascondi?:  'visible' |  'hidden';
		// events
		onhover?: (elem: HTMLElement) => void;
		// contained elements
		children: any;
		//...rest
		[key: string]: any;
	}
	let { direction = 'row',nascondi='visible', children, onhover, ...rest }: Props = $props();
	const onmousehover = (event: MouseEvent) => {
		onhover?.(event.currentTarget as HTMLElement);
	};
</script>

<!-- svelte-ignore a11y_no_static_element_interactions -->
<!-- svelte-ignore a11y_mouse_events_have_key_events -->
<div class="layout"  style:flex-direction={direction} style:visibility={nascondi} onmouseover={onmousehover} {...rest}>
	{@render children()}
</div>

cd
<style>
	.layout {
		background-color: aqua;
		display: flex;
		justify-content: center; /*allinea orizzontalmente*/
		align-items: center; /* allinea verticalmente */		
	}
</style>
