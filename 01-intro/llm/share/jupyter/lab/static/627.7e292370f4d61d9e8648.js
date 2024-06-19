/*! For license information please see 627.7e292370f4d61d9e8648.js.LICENSE.txt */
"use strict";(self["webpackChunk_jupyterlab_application_top"]=self["webpackChunk_jupyterlab_application_top"]||[]).push([[627],{30627:(e,t,o)=>{o.r(t);o.d(t,{Accordion:()=>it.Accordion,AccordionItem:()=>it.AccordionItem,Anchor:()=>_a,AnchoredRegion:()=>it.AnchoredRegion,Avatar:()=>Ja,Badge:()=>it.Badge,Breadcrumb:()=>it.Breadcrumb,BreadcrumbItem:()=>it.BreadcrumbItem,Button:()=>Zi,Card:()=>tl,Checkbox:()=>it.Checkbox,Combobox:()=>hl,ContrastTarget:()=>Fn,DataGrid:()=>it.DataGrid,DataGridCell:()=>it.DataGridCell,DataGridRow:()=>it.DataGridRow,DateField:()=>ls,Dialog:()=>it.Dialog,DirectionalStyleSheetBehavior:()=>Sn,Divider:()=>it.Divider,ListboxElement:()=>it.ListboxElement,Menu:()=>it.Menu,MenuItem:()=>it.MenuItem,NumberField:()=>ks,Option:()=>it.ListboxOption,PaletteRGB:()=>ot,Progress:()=>it.BaseProgress,Radio:()=>it.Radio,RadioGroup:()=>it.RadioGroup,Search:()=>Is,Select:()=>Us,SliderLabel:()=>tc,StandardLuminance:()=>at,SwatchRGB:()=>Ze,Tab:()=>it.Tab,TabPanel:()=>it.TabPanel,Tabs:()=>it.Tabs,TextArea:()=>pc,TextField:()=>xc,Toolbar:()=>kc,Tooltip:()=>it.Tooltip,accentColor:()=>_o,accentFillActive:()=>sr,accentFillActiveDelta:()=>po,accentFillFocus:()=>cr,accentFillFocusDelta:()=>go,accentFillHover:()=>lr,accentFillHoverDelta:()=>uo,accentFillRecipe:()=>ar,accentFillRest:()=>ir,accentFillRestDelta:()=>ho,accentForegroundActive:()=>Tr,accentForegroundActiveDelta:()=>$o,accentForegroundFocus:()=>Cr,accentForegroundFocusDelta:()=>xo,accentForegroundHover:()=>Fr,accentForegroundHoverDelta:()=>fo,accentForegroundRecipe:()=>wr,accentForegroundRest:()=>kr,accentForegroundRestDelta:()=>bo,accentPalette:()=>Eo,accordionItemStyles:()=>ia,accordionStyles:()=>ra,addJupyterLabThemeChangeListener:()=>fn,allComponents:()=>Rc,anchorStyles:()=>Ga,anchoredRegionStyles:()=>Wa,applyJupyterTheme:()=>vn,avatarStyles:()=>oi,badgeStyles:()=>ni,baseErrorColor:()=>kn,baseHeightMultiplier:()=>Nt,baseHorizontalSpacingMultiplier:()=>At,baseLayerLuminance:()=>Rt,black:()=>wn,bodyFont:()=>Ht,breadcrumbItemStyles:()=>si,breadcrumbStyles:()=>ii,cardStyles:()=>el,checkboxStyles:()=>nl,comboboxStyles:()=>dl,controlCornerRadius:()=>Pt,dataGridCellStyles:()=>bl,dataGridRowStyles:()=>pl,dataGridStyles:()=>gl,dateFieldStyles:()=>cs,dateFieldTemplate:()=>ds,density:()=>It,designUnit:()=>Mt,dialogStyles:()=>us,direction:()=>Gt,disabledOpacity:()=>_t,dividerStyles:()=>gs,errorBase:()=>Dn,errorFillActive:()=>Nn,errorFillAlgorithm:()=>Tn,errorFillFocus:()=>An,errorFillHover:()=>Hn,errorFillRecipe:()=>zn,errorFillRest:()=>Ln,errorForegroundActive:()=>Qn,errorForegroundAlgorithm:()=>Cn,errorForegroundFocus:()=>ea,errorForegroundHover:()=>Kn,errorForegroundRecipe:()=>Yn,errorForegroundRest:()=>Jn,errorPalette:()=>On,fillColor:()=>rr,focusStrokeInner:()=>Kr,focusStrokeInnerRecipe:()=>Jr,focusStrokeOuter:()=>Yr,focusStrokeOuterRecipe:()=>Zr,focusStrokeWidth:()=>qt,foregroundOnAccentActive:()=>gr,foregroundOnAccentActiveLarge:()=>mr,foregroundOnAccentFocus:()=>br,foregroundOnAccentFocusLarge:()=>vr,foregroundOnAccentHover:()=>pr,foregroundOnAccentHoverLarge:()=>xr,foregroundOnAccentLargeRecipe:()=>fr,foregroundOnAccentRecipe:()=>hr,foregroundOnAccentRest:()=>ur,foregroundOnAccentRestLarge:()=>$r,foregroundOnErrorActive:()=>Gn,foregroundOnErrorActiveLarge:()=>Un,foregroundOnErrorAlgorithm:()=>Vn,foregroundOnErrorFocus:()=>_n,foregroundOnErrorFocusLarge:()=>Xn,foregroundOnErrorHover:()=>Mn,foregroundOnErrorHoverLarge:()=>Wn,foregroundOnErrorLargeRecipe:()=>En,foregroundOnErrorRecipe:()=>Pn,foregroundOnErrorRest:()=>In,foregroundOnErrorRestLarge:()=>qn,horizontalSliderLabelStyles:()=>Ks,imgTemplate:()=>Ka,isDark:()=>se,jpAccordion:()=>sa,jpAccordionItem:()=>la,jpAnchor:()=>qa,jpAnchoredRegion:()=>Ua,jpAvatar:()=>ri,jpBadge:()=>ai,jpBreadcrumb:()=>li,jpBreadcrumbItem:()=>ci,jpButton:()=>Yi,jpCard:()=>rl,jpCheckbox:()=>al,jpCombobox:()=>ul,jpDataGrid:()=>xl,jpDataGridCell:()=>fl,jpDataGridRow:()=>$l,jpDateField:()=>hs,jpDialog:()=>ps,jpDivider:()=>bs,jpListbox:()=>$s,jpMenu:()=>ms,jpMenuItem:()=>ys,jpNumberField:()=>Cs,jpOption:()=>Ds,jpProgress:()=>js,jpProgressRing:()=>Os,jpRadio:()=>Ls,jpRadioGroup:()=>Ns,jpSearch:()=>Ws,jpSelect:()=>Xs,jpSlider:()=>Ys,jpSliderLabel:()=>rc,jpSwitch:()=>ac,jpTab:()=>cc,jpTabPanel:()=>lc,jpTabs:()=>hc,jpTextArea:()=>fc,jpTextField:()=>yc,jpToolbar:()=>Cc,jpTooltip:()=>Dc,jpTreeItem:()=>Hc,jpTreeView:()=>Ac,listboxStyles:()=>fs,menuItemStyles:()=>vs,menuStyles:()=>xs,neutralColor:()=>Mo,neutralFillActive:()=>jr,neutralFillActiveDelta:()=>yo,neutralFillFocus:()=>Br,neutralFillFocusDelta:()=>wo,neutralFillHover:()=>Sr,neutralFillHoverDelta:()=>vo,neutralFillInputActive:()=>Hr,neutralFillInputActiveDelta:()=>To,neutralFillInputFocus:()=>Nr,neutralFillInputFocusDelta:()=>Co,neutralFillInputHover:()=>Lr,neutralFillInputHoverDelta:()=>Fo,neutralFillInputRecipe:()=>Or,neutralFillInputRest:()=>zr,neutralFillInputRestDelta:()=>ko,neutralFillLayerRecipe:()=>Ur,neutralFillLayerRest:()=>Xr,neutralFillLayerRestDelta:()=>Ho,neutralFillRecipe:()=>Vr,neutralFillRest:()=>Dr,neutralFillRestDelta:()=>mo,neutralFillStealthActive:()=>Ir,neutralFillStealthActiveDelta:()=>So,neutralFillStealthFocus:()=>Mr,neutralFillStealthFocusDelta:()=>jo,neutralFillStealthHover:()=>Pr,neutralFillStealthHoverDelta:()=>Do,neutralFillStealthRecipe:()=>Ar,neutralFillStealthRest:()=>Rr,neutralFillStealthRestDelta:()=>Vo,neutralFillStrongActive:()=>qr,neutralFillStrongActiveDelta:()=>zo,neutralFillStrongFocus:()=>Wr,neutralFillStrongFocusDelta:()=>Lo,neutralFillStrongHover:()=>Er,neutralFillStrongHoverDelta:()=>Oo,neutralFillStrongRecipe:()=>Gr,neutralFillStrongRest:()=>_r,neutralFillStrongRestDelta:()=>Bo,neutralForegroundHint:()=>en,neutralForegroundHintRecipe:()=>Qr,neutralForegroundRecipe:()=>tn,neutralForegroundRest:()=>on,neutralLayer1:()=>Yo,neutralLayer1Recipe:()=>Zo,neutralLayer2:()=>Ko,neutralLayer2Recipe:()=>Jo,neutralLayer3:()=>er,neutralLayer3Recipe:()=>Qo,neutralLayer4:()=>or,neutralLayer4Recipe:()=>tr,neutralLayerCardContainer:()=>Wo,neutralLayerCardContainerRecipe:()=>qo,neutralLayerFloating:()=>Xo,neutralLayerFloatingRecipe:()=>Uo,neutralPalette:()=>Go,neutralStrokeActive:()=>ln,neutralStrokeActiveDelta:()=>Ro,neutralStrokeDividerRecipe:()=>cn,neutralStrokeDividerRest:()=>dn,neutralStrokeDividerRestDelta:()=>Io,neutralStrokeFocus:()=>sn,neutralStrokeFocusDelta:()=>Po,neutralStrokeHover:()=>an,neutralStrokeHoverDelta:()=>Ao,neutralStrokeRecipe:()=>rn,neutralStrokeRest:()=>nn,neutralStrokeRestDelta:()=>No,numberFieldStyles:()=>Ts,optionStyles:()=>Vs,progressStyles:()=>Ss,provideJupyterDesignSystem:()=>ta,radioGroupStyles:()=>Hs,radioStyles:()=>zs,searchStyles:()=>qs,selectStyles:()=>cl,sliderLabelStyles:()=>ec,strokeWidth:()=>Et,tabPanelStyles:()=>ic,tabStyles:()=>sc,tabsStyles:()=>dc,textAreaStyles:()=>bc,textFieldStyles:()=>vc,toolbarStyles:()=>Tc,tooltipStyles:()=>Vc,typeRampBaseFontSize:()=>Wt,typeRampBaseLineHeight:()=>Ut,typeRampMinus1FontSize:()=>Xt,typeRampMinus1LineHeight:()=>Zt,typeRampMinus2FontSize:()=>Yt,typeRampMinus2LineHeight:()=>Jt,typeRampPlus1FontSize:()=>Kt,typeRampPlus1LineHeight:()=>Qt,typeRampPlus2FontSize:()=>eo,typeRampPlus2LineHeight:()=>to,typeRampPlus3FontSize:()=>oo,typeRampPlus3LineHeight:()=>ro,typeRampPlus4FontSize:()=>no,typeRampPlus4LineHeight:()=>ao,typeRampPlus5FontSize:()=>io,typeRampPlus5LineHeight:()=>lo,typeRampPlus6FontSize:()=>so,typeRampPlus6LineHeight:()=>co,verticalSliderLabelStyles:()=>Qs,white:()=>yn});function r(e,t,o){if(isNaN(e)||e<=t){return t}else if(e>=o){return o}return e}function n(e,t,o){if(isNaN(e)||e<=t){return 0}else if(e>=o){return 1}return e/(o-t)}function a(e,t,o){if(isNaN(e)){return t}return t+e*(o-t)}function i(e){return e*(Math.PI/180)}function l(e){return e*(180/Math.PI)}function s(e){const t=Math.round(r(e,0,255)).toString(16);if(t.length===1){return"0"+t}return t}function c(e,t,o){if(isNaN(e)||e<=0){return t}else if(e>=1){return o}return t+e*(o-t)}function d(e,t,o){if(e<=0){return t%360}else if(e>=1){return o%360}const r=(t-o+360)%360;const n=(o-t+360)%360;if(r<=n){return(t-r*e+360)%360}return(t+r*e+360)%360}const h=Math.PI*2;function u(e,t,o){if(isNaN(e)||e<=0){return t%h}else if(e>=1){return o%h}const r=(t-o+h)%h;const n=(o-t+h)%h;if(r<=n){return(t-r*e+h)%h}return(t+r*e+h)%h}function p(e,t){const o=Math.pow(10,t);return Math.round(e*o)/o}class g{constructor(e,t,o,r){this.r=e;this.g=t;this.b=o;this.a=typeof r==="number"&&!isNaN(r)?r:1}static fromObject(e){return e&&!isNaN(e.r)&&!isNaN(e.g)&&!isNaN(e.b)?new g(e.r,e.g,e.b,e.a):null}equalValue(e){return this.r===e.r&&this.g===e.g&&this.b===e.b&&this.a===e.a}toStringHexRGB(){return"#"+[this.r,this.g,this.b].map(this.formatHexValue).join("")}toStringHexRGBA(){return this.toStringHexRGB()+this.formatHexValue(this.a)}toStringHexARGB(){return"#"+[this.a,this.r,this.g,this.b].map(this.formatHexValue).join("")}toStringWebRGB(){return`rgb(${Math.round(a(this.r,0,255))},${Math.round(a(this.g,0,255))},${Math.round(a(this.b,0,255))})`}toStringWebRGBA(){return`rgba(${Math.round(a(this.r,0,255))},${Math.round(a(this.g,0,255))},${Math.round(a(this.b,0,255))},${r(this.a,0,1)})`}roundToPrecision(e){return new g(p(this.r,e),p(this.g,e),p(this.b,e),p(this.a,e))}clamp(){return new g(r(this.r,0,1),r(this.g,0,1),r(this.b,0,1),r(this.a,0,1))}toObject(){return{r:this.r,g:this.g,b:this.b,a:this.a}}formatHexValue(e){return s(a(e,0,255))}}const b={aliceblue:{r:.941176,g:.972549,b:1},antiquewhite:{r:.980392,g:.921569,b:.843137},aqua:{r:0,g:1,b:1},aquamarine:{r:.498039,g:1,b:.831373},azure:{r:.941176,g:1,b:1},beige:{r:.960784,g:.960784,b:.862745},bisque:{r:1,g:.894118,b:.768627},black:{r:0,g:0,b:0},blanchedalmond:{r:1,g:.921569,b:.803922},blue:{r:0,g:0,b:1},blueviolet:{r:.541176,g:.168627,b:.886275},brown:{r:.647059,g:.164706,b:.164706},burlywood:{r:.870588,g:.721569,b:.529412},cadetblue:{r:.372549,g:.619608,b:.627451},chartreuse:{r:.498039,g:1,b:0},chocolate:{r:.823529,g:.411765,b:.117647},coral:{r:1,g:.498039,b:.313725},cornflowerblue:{r:.392157,g:.584314,b:.929412},cornsilk:{r:1,g:.972549,b:.862745},crimson:{r:.862745,g:.078431,b:.235294},cyan:{r:0,g:1,b:1},darkblue:{r:0,g:0,b:.545098},darkcyan:{r:0,g:.545098,b:.545098},darkgoldenrod:{r:.721569,g:.52549,b:.043137},darkgray:{r:.662745,g:.662745,b:.662745},darkgreen:{r:0,g:.392157,b:0},darkgrey:{r:.662745,g:.662745,b:.662745},darkkhaki:{r:.741176,g:.717647,b:.419608},darkmagenta:{r:.545098,g:0,b:.545098},darkolivegreen:{r:.333333,g:.419608,b:.184314},darkorange:{r:1,g:.54902,b:0},darkorchid:{r:.6,g:.196078,b:.8},darkred:{r:.545098,g:0,b:0},darksalmon:{r:.913725,g:.588235,b:.478431},darkseagreen:{r:.560784,g:.737255,b:.560784},darkslateblue:{r:.282353,g:.239216,b:.545098},darkslategray:{r:.184314,g:.309804,b:.309804},darkslategrey:{r:.184314,g:.309804,b:.309804},darkturquoise:{r:0,g:.807843,b:.819608},darkviolet:{r:.580392,g:0,b:.827451},deeppink:{r:1,g:.078431,b:.576471},deepskyblue:{r:0,g:.74902,b:1},dimgray:{r:.411765,g:.411765,b:.411765},dimgrey:{r:.411765,g:.411765,b:.411765},dodgerblue:{r:.117647,g:.564706,b:1},firebrick:{r:.698039,g:.133333,b:.133333},floralwhite:{r:1,g:.980392,b:.941176},forestgreen:{r:.133333,g:.545098,b:.133333},fuchsia:{r:1,g:0,b:1},gainsboro:{r:.862745,g:.862745,b:.862745},ghostwhite:{r:.972549,g:.972549,b:1},gold:{r:1,g:.843137,b:0},goldenrod:{r:.854902,g:.647059,b:.12549},gray:{r:.501961,g:.501961,b:.501961},green:{r:0,g:.501961,b:0},greenyellow:{r:.678431,g:1,b:.184314},grey:{r:.501961,g:.501961,b:.501961},honeydew:{r:.941176,g:1,b:.941176},hotpink:{r:1,g:.411765,b:.705882},indianred:{r:.803922,g:.360784,b:.360784},indigo:{r:.294118,g:0,b:.509804},ivory:{r:1,g:1,b:.941176},khaki:{r:.941176,g:.901961,b:.54902},lavender:{r:.901961,g:.901961,b:.980392},lavenderblush:{r:1,g:.941176,b:.960784},lawngreen:{r:.486275,g:.988235,b:0},lemonchiffon:{r:1,g:.980392,b:.803922},lightblue:{r:.678431,g:.847059,b:.901961},lightcoral:{r:.941176,g:.501961,b:.501961},lightcyan:{r:.878431,g:1,b:1},lightgoldenrodyellow:{r:.980392,g:.980392,b:.823529},lightgray:{r:.827451,g:.827451,b:.827451},lightgreen:{r:.564706,g:.933333,b:.564706},lightgrey:{r:.827451,g:.827451,b:.827451},lightpink:{r:1,g:.713725,b:.756863},lightsalmon:{r:1,g:.627451,b:.478431},lightseagreen:{r:.12549,g:.698039,b:.666667},lightskyblue:{r:.529412,g:.807843,b:.980392},lightslategray:{r:.466667,g:.533333,b:.6},lightslategrey:{r:.466667,g:.533333,b:.6},lightsteelblue:{r:.690196,g:.768627,b:.870588},lightyellow:{r:1,g:1,b:.878431},lime:{r:0,g:1,b:0},limegreen:{r:.196078,g:.803922,b:.196078},linen:{r:.980392,g:.941176,b:.901961},magenta:{r:1,g:0,b:1},maroon:{r:.501961,g:0,b:0},mediumaquamarine:{r:.4,g:.803922,b:.666667},mediumblue:{r:0,g:0,b:.803922},mediumorchid:{r:.729412,g:.333333,b:.827451},mediumpurple:{r:.576471,g:.439216,b:.858824},mediumseagreen:{r:.235294,g:.701961,b:.443137},mediumslateblue:{r:.482353,g:.407843,b:.933333},mediumspringgreen:{r:0,g:.980392,b:.603922},mediumturquoise:{r:.282353,g:.819608,b:.8},mediumvioletred:{r:.780392,g:.082353,b:.521569},midnightblue:{r:.098039,g:.098039,b:.439216},mintcream:{r:.960784,g:1,b:.980392},mistyrose:{r:1,g:.894118,b:.882353},moccasin:{r:1,g:.894118,b:.709804},navajowhite:{r:1,g:.870588,b:.678431},navy:{r:0,g:0,b:.501961},oldlace:{r:.992157,g:.960784,b:.901961},olive:{r:.501961,g:.501961,b:0},olivedrab:{r:.419608,g:.556863,b:.137255},orange:{r:1,g:.647059,b:0},orangered:{r:1,g:.270588,b:0},orchid:{r:.854902,g:.439216,b:.839216},palegoldenrod:{r:.933333,g:.909804,b:.666667},palegreen:{r:.596078,g:.984314,b:.596078},paleturquoise:{r:.686275,g:.933333,b:.933333},palevioletred:{r:.858824,g:.439216,b:.576471},papayawhip:{r:1,g:.937255,b:.835294},peachpuff:{r:1,g:.854902,b:.72549},peru:{r:.803922,g:.521569,b:.247059},pink:{r:1,g:.752941,b:.796078},plum:{r:.866667,g:.627451,b:.866667},powderblue:{r:.690196,g:.878431,b:.901961},purple:{r:.501961,g:0,b:.501961},red:{r:1,g:0,b:0},rosybrown:{r:.737255,g:.560784,b:.560784},royalblue:{r:.254902,g:.411765,b:.882353},saddlebrown:{r:.545098,g:.270588,b:.07451},salmon:{r:.980392,g:.501961,b:.447059},sandybrown:{r:.956863,g:.643137,b:.376471},seagreen:{r:.180392,g:.545098,b:.341176},seashell:{r:1,g:.960784,b:.933333},sienna:{r:.627451,g:.321569,b:.176471},silver:{r:.752941,g:.752941,b:.752941},skyblue:{r:.529412,g:.807843,b:.921569},slateblue:{r:.415686,g:.352941,b:.803922},slategray:{r:.439216,g:.501961,b:.564706},slategrey:{r:.439216,g:.501961,b:.564706},snow:{r:1,g:.980392,b:.980392},springgreen:{r:0,g:1,b:.498039},steelblue:{r:.27451,g:.509804,b:.705882},tan:{r:.823529,g:.705882,b:.54902},teal:{r:0,g:.501961,b:.501961},thistle:{r:.847059,g:.74902,b:.847059},tomato:{r:1,g:.388235,b:.278431},transparent:{r:0,g:0,b:0,a:0},turquoise:{r:.25098,g:.878431,b:.815686},violet:{r:.933333,g:.509804,b:.933333},wheat:{r:.960784,g:.870588,b:.701961},white:{r:1,g:1,b:1},whitesmoke:{r:.960784,g:.960784,b:.960784},yellow:{r:1,g:1,b:0},yellowgreen:{r:.603922,g:.803922,b:.196078}};const f=/^rgb\(\s*((?:(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*,\s*){2}(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*)\)$/i;const $=/^rgba\(\s*((?:(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\s*,\s*){3}(?:0|1|0?\.\d*)\s*)\)$/i;const x=/^#((?:[0-9a-f]{6}|[0-9a-f]{3}))$/i;const m=/^#((?:[0-9a-f]{8}|[0-9a-f]{4}))$/i;function v(e){return x.test(e)}function y(e){return m.test(e)}function w(e){return y(e)}function k(e){return f.test(e)}function F(e){return $.test(e)}function T(e){return b.hasOwnProperty(e)}function C(e){const t=x.exec(e);if(t===null){return null}let o=t[1];if(o.length===3){const e=o.charAt(0);const t=o.charAt(1);const r=o.charAt(2);o=e.concat(e,t,t,r,r)}const r=parseInt(o,16);if(isNaN(r)){return null}return new g(n((r&16711680)>>>16,0,255),n((r&65280)>>>8,0,255),n(r&255,0,255),1)}function V(e){const t=m.exec(e);if(t===null){return null}let o=t[1];if(o.length===4){const e=o.charAt(0);const t=o.charAt(1);const r=o.charAt(2);const n=o.charAt(3);o=e.concat(e,t,t,r,r,n,n)}const r=parseInt(o,16);if(isNaN(r)){return null}return new g(n((r&16711680)>>>16,0,255),n((r&65280)>>>8,0,255),n(r&255,0,255),n((r&4278190080)>>>24,0,255))}function D(e){const t=m.exec(e);if(t===null){return null}let o=t[1];if(o.length===4){const e=o.charAt(0);const t=o.charAt(1);const r=o.charAt(2);const n=o.charAt(3);o=e.concat(e,t,t,r,r,n,n)}const r=parseInt(o,16);if(isNaN(r)){return null}return new ColorRGBA64(normalize((r&4278190080)>>>24,0,255),normalize((r&16711680)>>>16,0,255),normalize((r&65280)>>>8,0,255),normalize(r&255,0,255))}function S(e){const t=f.exec(e);if(t===null){return null}const o=t[1].split(",");return new g(n(Number(o[0]),0,255),n(Number(o[1]),0,255),n(Number(o[2]),0,255),1)}function j(e){const t=$.exec(e);if(t===null){return null}const o=t[1].split(",");if(o.length===4){return new g(n(Number(o[0]),0,255),n(Number(o[1]),0,255),n(Number(o[2]),0,255),Number(o[3]))}return null}function B(e){const t=b[e.toLowerCase()];return t?new g(t.r,t.g,t.b,t.hasOwnProperty("a")?t.a:void 0):null}function O(e){const t=e.toLowerCase();return v(t)?C(t):w(t)?V(t):k(t)?S(t):F(t)?j(t):T(t)?B(t):null}class z{constructor(e,t,o){this.h=e;this.s=t;this.l=o}static fromObject(e){if(e&&!isNaN(e.h)&&!isNaN(e.s)&&!isNaN(e.l)){return new z(e.h,e.s,e.l)}return null}equalValue(e){return this.h===e.h&&this.s===e.s&&this.l===e.l}roundToPrecision(e){return new z(p(this.h,e),p(this.s,e),p(this.l,e))}toObject(){return{h:this.h,s:this.s,l:this.l}}}class L{constructor(e,t,o){this.h=e;this.s=t;this.v=o}static fromObject(e){if(e&&!isNaN(e.h)&&!isNaN(e.s)&&!isNaN(e.v)){return new L(e.h,e.s,e.v)}return null}equalValue(e){return this.h===e.h&&this.s===e.s&&this.v===e.v}roundToPrecision(e){return new L(p(this.h,e),p(this.s,e),p(this.v,e))}toObject(){return{h:this.h,s:this.s,v:this.v}}}class H{constructor(e,t,o){this.l=e;this.a=t;this.b=o}static fromObject(e){if(e&&!isNaN(e.l)&&!isNaN(e.a)&&!isNaN(e.b)){return new H(e.l,e.a,e.b)}return null}equalValue(e){return this.l===e.l&&this.a===e.a&&this.b===e.b}roundToPrecision(e){return new H(p(this.l,e),p(this.a,e),p(this.b,e))}toObject(){return{l:this.l,a:this.a,b:this.b}}}H.epsilon=216/24389;H.kappa=24389/27;class N{constructor(e,t,o){this.l=e;this.c=t;this.h=o}static fromObject(e){if(e&&!isNaN(e.l)&&!isNaN(e.c)&&!isNaN(e.h)){return new N(e.l,e.c,e.h)}return null}equalValue(e){return this.l===e.l&&this.c===e.c&&this.h===e.h}roundToPrecision(e){return new N(p(this.l,e),p(this.c,e),p(this.h,e))}toObject(){return{l:this.l,c:this.c,h:this.h}}}class A{constructor(e,t,o){this.x=e;this.y=t;this.z=o}static fromObject(e){if(e&&!isNaN(e.x)&&!isNaN(e.y)&&!isNaN(e.z)){return new A(e.x,e.y,e.z)}return null}equalValue(e){return this.x===e.x&&this.y===e.y&&this.z===e.z}roundToPrecision(e){return new A(p(this.x,e),p(this.y,e),p(this.z,e))}toObject(){return{x:this.x,y:this.y,z:this.z}}}A.whitePoint=new A(.95047,1,1.08883);function R(e){return e.r*.2126+e.g*.7152+e.b*.0722}function P(e){function t(e){if(e<=.03928){return e/12.92}return Math.pow((e+.055)/1.055,2.4)}return R(new g(t(e.r),t(e.g),t(e.b),1))}const I=(e,t)=>(e+.05)/(t+.05);function M(e,t){const o=P(e);const r=P(t);return o>r?I(o,r):I(r,o)}function G(e,t,o){if(o-t===0){return 0}else{return(e-t)/(o-t)}}function _(e,t,o){const r=G(e.r,t.r,o.r);const n=G(e.g,t.g,o.g);const a=G(e.b,t.b,o.b);return(r+n+a)/3}function E(e,t,o=null){let r=0;let n=o;if(n!==null){r=_(e,t,n)}else{n=new ColorRGBA64(0,0,0,1);r=_(e,t,n);if(r<=0){n=new ColorRGBA64(1,1,1,1);r=_(e,t,n)}}r=Math.round(r*1e3)/1e3;return new ColorRGBA64(n.r,n.g,n.b,r)}function q(e){const t=Math.max(e.r,e.g,e.b);const o=Math.min(e.r,e.g,e.b);const r=t-o;let n=0;if(r!==0){if(t===e.r){n=60*((e.g-e.b)/r%6)}else if(t===e.g){n=60*((e.b-e.r)/r+2)}else{n=60*((e.r-e.g)/r+4)}}if(n<0){n+=360}const a=(t+o)/2;let i=0;if(r!==0){i=r/(1-Math.abs(2*a-1))}return new z(n,i,a)}function W(e,t=1){const o=(1-Math.abs(2*e.l-1))*e.s;const r=o*(1-Math.abs(e.h/60%2-1));const n=e.l-o/2;let a=0;let i=0;let l=0;if(e.h<60){a=o;i=r;l=0}else if(e.h<120){a=r;i=o;l=0}else if(e.h<180){a=0;i=o;l=r}else if(e.h<240){a=0;i=r;l=o}else if(e.h<300){a=r;i=0;l=o}else if(e.h<360){a=o;i=0;l=r}return new g(a+n,i+n,l+n,t)}function U(e){const t=Math.max(e.r,e.g,e.b);const o=Math.min(e.r,e.g,e.b);const r=t-o;let n=0;if(r!==0){if(t===e.r){n=60*((e.g-e.b)/r%6)}else if(t===e.g){n=60*((e.b-e.r)/r+2)}else{n=60*((e.r-e.g)/r+4)}}if(n<0){n+=360}let a=0;if(t!==0){a=r/t}return new L(n,a,t)}function X(e,t=1){const o=e.s*e.v;const r=o*(1-Math.abs(e.h/60%2-1));const n=e.v-o;let a=0;let i=0;let l=0;if(e.h<60){a=o;i=r;l=0}else if(e.h<120){a=r;i=o;l=0}else if(e.h<180){a=0;i=o;l=r}else if(e.h<240){a=0;i=r;l=o}else if(e.h<300){a=r;i=0;l=o}else if(e.h<360){a=o;i=0;l=r}return new g(a+n,i+n,l+n,t)}function Z(e){let t=0;let o=0;if(e.h!==0){t=Math.cos(i(e.h))*e.c;o=Math.sin(i(e.h))*e.c}return new H(e.l,t,o)}function Y(e){let t=0;if(Math.abs(e.b)>.001||Math.abs(e.a)>.001){t=l(Math.atan2(e.b,e.a))}if(t<0){t+=360}const o=Math.sqrt(e.a*e.a+e.b*e.b);return new N(e.l,o,t)}function J(e){const t=(e.l+16)/116;const o=t+e.a/500;const r=t-e.b/200;const n=Math.pow(o,3);const a=Math.pow(t,3);const i=Math.pow(r,3);let l=0;if(n>H.epsilon){l=n}else{l=(116*o-16)/H.kappa}let s=0;if(e.l>H.epsilon*H.kappa){s=a}else{s=e.l/H.kappa}let c=0;if(i>H.epsilon){c=i}else{c=(116*r-16)/H.kappa}l=A.whitePoint.x*l;s=A.whitePoint.y*s;c=A.whitePoint.z*c;return new A(l,s,c)}function K(e){function t(e){if(e>H.epsilon){return Math.pow(e,1/3)}return(H.kappa*e+16)/116}const o=t(e.x/A.whitePoint.x);const r=t(e.y/A.whitePoint.y);const n=t(e.z/A.whitePoint.z);const a=116*r-16;const i=500*(o-r);const l=200*(r-n);return new H(a,i,l)}function Q(e){function t(e){if(e<=.04045){return e/12.92}return Math.pow((e+.055)/1.055,2.4)}const o=t(e.r);const r=t(e.g);const n=t(e.b);const a=o*.4124564+r*.3575761+n*.1804375;const i=o*.2126729+r*.7151522+n*.072175;const l=o*.0193339+r*.119192+n*.9503041;return new A(a,i,l)}function ee(e,t=1){function o(e){if(e<=.0031308){return e*12.92}return 1.055*Math.pow(e,1/2.4)-.055}const r=o(e.x*3.2404542-e.y*1.5371385-e.z*.4985314);const n=o(e.x*-.969266+e.y*1.8760108+e.z*.041556);const a=o(e.x*.0556434-e.y*.2040259+e.z*1.0572252);return new g(r,n,a,t)}function te(e){return K(Q(e))}function oe(e,t=1){return ee(J(e),t)}function re(e){return Y(te(e))}function ne(e,t=1){return oe(Z(e),t)}function ae(e,t=1){let o=0;let r=0;let n=0;if(e<=1e3){e=1e3}else if(e>=4e4){e=4e4}if(e<6600){o=255;r=e/100-2;r=-155.25485562709179-.44596950469579133*r+104.49216199393888*Math.log(r)}else{o=e/100-55;o=351.97690566805693+.114206453784165*o-40.25366309332127*Math.log(o);r=e/100-50;r=325.4494125711974+.07943456536662342*r-28.0852963507957*Math.log(r)}if(e>=6600){n=255}else if(e<2e3){n=0}else{n=e/100-10;n=-254.76935184120902+.8274096064007395*n+115.67994401066147*Math.log(n)}return new ColorRGBA64(o/255,r/255,n/255,t)}function ie(e){let t=0;let o=1e3;let r=4e4;while(r-o>.4){t=(r+o)/2;const n=ae(t);if(n.b/n.r>=e.b/e.r){r=t}else{o=t}}return Math.round(t)}const le=(-.1+Math.sqrt(.21))/2;function se(e){return e.relativeLuminance<=le}function ce(e,t,o=18){const r=re(e);let n=r.c+t*o;if(n<0){n=0}return ne(new N(r.l,n,r.h))}function de(e,t,o=18){return ce(e,-1*t,o)}function he(e,t,o=18){const r=rgbToLAB(e);const n=r.l-t*o;return labToRGB(new ColorLAB(n,r.a,r.b))}function ue(e,t,o=18){return he(e,-1*t,o)}function pe(e,t){if(t===0){return 0}return 1-(1-e)/t}function ge(e,t){return new ColorRGBA64(pe(e.r,t.r),pe(e.g,t.g),pe(e.b,t.b),1)}function be(e,t){const o=rgbToHSL(e);const r=rgbToHSL(t);if(r.s===0){return new ColorRGBA64(o.l,o.l,o.l,1)}return hslToRGB(new ColorHSL(r.h,r.s,o.l))}function fe(e,t){return Math.min(e,t)}function $e(e,t){return new ColorRGBA64(fe(e.r,t.r),fe(e.g,t.g),fe(e.b,t.b),1)}function xe(e,t){if(t>=1){return 1}const o=e/(1-t);if(o>=1){return 1}return o}function me(e,t){return new ColorRGBA64(xe(e.r,t.r),xe(e.g,t.g),xe(e.b,t.b),1)}function ve(e,t){return Math.max(e,t)}function ye(e,t){return new ColorRGBA64(ve(e.r,t.r),ve(e.g,t.g),ve(e.b,t.b),1)}function we(e,t){return e*t}function ke(e,t){return new g(we(e.r,t.r),we(e.g,t.g),we(e.b,t.b),1)}function Fe(e,t){if(e<.5){return r(2*t*e,0,1)}return r(1-2*(1-t)*(1-e),0,1)}function Te(e,t){return new g(Fe(e.r,t.r),Fe(e.g,t.g),Fe(e.b,t.b),1)}function Ce(e,t){return 1-(1-t)*(1-e)}function Ve(e,t){return new ColorRGBA64(Ce(e.r,t.r),Ce(e.g,t.g),Ce(e.b,t.b),1)}var De;(function(e){e[e["Burn"]=0]="Burn";e[e["Color"]=1]="Color";e[e["Darken"]=2]="Darken";e[e["Dodge"]=3]="Dodge";e[e["Lighten"]=4]="Lighten";e[e["Multiply"]=5]="Multiply";e[e["Overlay"]=6]="Overlay";e[e["Screen"]=7]="Screen"})(De||(De={}));function Se(e,t,o){switch(e){case De.Burn:return ge(t,o);case De.Color:return be(t,o);case De.Darken:return $e(t,o);case De.Dodge:return me(t,o);case De.Lighten:return ye(t,o);case De.Multiply:return ke(t,o);case De.Overlay:return Te(t,o);case De.Screen:return Ve(t,o);default:throw new Error("Unknown blend mode")}}function je(e,t){if(t.a>=1){return t}else if(t.a<=0){return new ColorRGBA64(e.r,e.g,e.b,1)}const o=t.a*t.r+(1-t.a)*e.r;const r=t.a*t.g+(1-t.a)*e.g;const n=t.a*t.b+(1-t.a)*e.b;return new ColorRGBA64(o,r,n,1)}function Be(e,t,o){if(isNaN(e)||e<=0){return t}else if(e>=1){return o}return new g(c(e,t.r,o.r),c(e,t.g,o.g),c(e,t.b,o.b),c(e,t.a,o.a))}function Oe(e,t,o){if(isNaN(e)||e<=0){return t}else if(e>=1){return o}return new z(d(e,t.h,o.h),c(e,t.s,o.s),c(e,t.l,o.l))}function ze(e,t,o){if(isNaN(e)||e<=0){return t}else if(e>=1){return o}return new L(d(e,t.h,o.h),c(e,t.s,o.s),c(e,t.v,o.v))}function Le(e,t,o){if(isNaN(e)||e<=0){return t}else if(e>=1){return o}return new A(c(e,t.x,o.x),c(e,t.y,o.y),c(e,t.z,o.z))}function He(e,t,o){if(isNaN(e)||e<=0){return t}else if(e>=1){return o}return new H(c(e,t.l,o.l),c(e,t.a,o.a),c(e,t.b,o.b))}function Ne(e,t,o){if(isNaN(e)||e<=0){return t}else if(e>=1){return o}return new N(c(e,t.l,o.l),c(e,t.c,o.c),d(e,t.h,o.h))}var Ae;(function(e){e[e["RGB"]=0]="RGB";e[e["HSL"]=1]="HSL";e[e["HSV"]=2]="HSV";e[e["XYZ"]=3]="XYZ";e[e["LAB"]=4]="LAB";e[e["LCH"]=5]="LCH"})(Ae||(Ae={}));function Re(e,t,o,r){if(isNaN(e)||e<=0){return o}else if(e>=1){return r}switch(t){case Ae.HSL:return W(Oe(e,q(o),q(r)));case Ae.HSV:return X(ze(e,U(o),U(r)));case Ae.XYZ:return ee(Le(e,Q(o),Q(r)));case Ae.LAB:return oe(He(e,te(o),te(r)));case Ae.LCH:return ne(Ne(e,re(o),re(r)));default:return Be(e,o,r)}}class Pe{constructor(e){if(e==null||e.length===0){throw new Error("The stops argument must be non-empty")}else{this.stops=this.sortColorScaleStops(e)}}static createBalancedColorScale(e){if(e==null||e.length===0){throw new Error("The colors argument must be non-empty")}const t=new Array(e.length);for(let o=0;o<e.length;o++){if(o===0){t[o]={color:e[o],position:0}}else if(o===e.length-1){t[o]={color:e[o],position:1}}else{t[o]={color:e[o],position:o*(1/(e.length-1))}}}return new Pe(t)}getColor(e,t=Ae.RGB){if(this.stops.length===1){return this.stops[0].color}else if(e<=0){return this.stops[0].color}else if(e>=1){return this.stops[this.stops.length-1].color}let o=0;for(let a=0;a<this.stops.length;a++){if(this.stops[a].position<=e){o=a}}let r=o+1;if(r>=this.stops.length){r=this.stops.length-1}const n=(e-this.stops[o].position)*(1/(this.stops[r].position-this.stops[o].position));return Re(n,t,this.stops[o].color,this.stops[r].color)}trim(e,t,o=Ae.RGB){if(e<0||t>1||t<e){throw new Error("Invalid bounds")}if(e===t){return new Pe([{color:this.getColor(e,o),position:0}])}const r=[];for(let i=0;i<this.stops.length;i++){if(this.stops[i].position>=e&&this.stops[i].position<=t){r.push(this.stops[i])}}if(r.length===0){return new Pe([{color:this.getColor(e),position:e},{color:this.getColor(t),position:t}])}if(r[0].position!==e){r.unshift({color:this.getColor(e),position:e})}if(r[r.length-1].position!==t){r.push({color:this.getColor(t),position:t})}const n=t-e;const a=new Array(r.length);for(let i=0;i<r.length;i++){a[i]={color:r[i].color,position:(r[i].position-e)/n}}return new Pe(a)}findNextColor(e,t,o=false,r=Ae.RGB,n=.005,a=32){if(isNaN(e)||e<=0){e=0}else if(e>=1){e=1}const i=this.getColor(e,r);const l=o?0:1;const s=this.getColor(l,r);const c=M(i,s);if(c<=t){return l}let d=o?0:e;let h=o?e:0;let u=l;let p=0;while(p<=a){u=Math.abs(h-d)/2+d;const e=this.getColor(u,r);const a=M(i,e);if(Math.abs(a-t)<=n){return u}else if(a>t){if(o){d=u}else{h=u}}else{if(o){h=u}else{d=u}}p++}return u}clone(){const e=new Array(this.stops.length);for(let t=0;t<e.length;t++){e[t]={color:this.stops[t].color,position:this.stops[t].position}}return new Pe(e)}sortColorScaleStops(e){return e.sort(((e,t)=>{const o=e.position;const r=t.position;if(o<r){return-1}else if(o>r){return 1}else{return 0}}))}}class Ie{constructor(e){this.config=Object.assign({},Ie.defaultPaletteConfig,e);this.palette=[];this.updatePaletteColors()}updatePaletteGenerationValues(e){let t=false;for(const o in e){if(this.config[o]){if(this.config[o].equalValue){if(!this.config[o].equalValue(e[o])){this.config[o]=e[o];t=true}}else{if(e[o]!==this.config[o]){this.config[o]=e[o];t=true}}}}if(t){this.updatePaletteColors()}return t}updatePaletteColors(){const e=this.generatePaletteColorScale();for(let t=0;t<this.config.steps;t++){this.palette[t]=e.getColor(t/(this.config.steps-1),this.config.interpolationMode)}}generatePaletteColorScale(){const e=q(this.config.baseColor);const t=new Pe([{position:0,color:this.config.scaleColorLight},{position:.5,color:this.config.baseColor},{position:1,color:this.config.scaleColorDark}]);const o=t.trim(this.config.clipLight,1-this.config.clipDark);const r=o.getColor(0);const n=o.getColor(1);let a=r;let i=n;if(e.s>=this.config.saturationAdjustmentCutoff){a=ce(a,this.config.saturationLight);i=ce(i,this.config.saturationDark)}if(this.config.multiplyLight!==0){const e=ke(this.config.baseColor,a);a=Re(this.config.multiplyLight,this.config.interpolationMode,a,e)}if(this.config.multiplyDark!==0){const e=ke(this.config.baseColor,i);i=Re(this.config.multiplyDark,this.config.interpolationMode,i,e)}if(this.config.overlayLight!==0){const e=Te(this.config.baseColor,a);a=Re(this.config.overlayLight,this.config.interpolationMode,a,e)}if(this.config.overlayDark!==0){const e=Te(this.config.baseColor,i);i=Re(this.config.overlayDark,this.config.interpolationMode,i,e)}if(this.config.baseScalePosition){if(this.config.baseScalePosition<=0){return new Pe([{position:0,color:this.config.baseColor},{position:1,color:i.clamp()}])}else if(this.config.baseScalePosition>=1){return new Pe([{position:0,color:a.clamp()},{position:1,color:this.config.baseColor}])}return new Pe([{position:0,color:a.clamp()},{position:this.config.baseScalePosition,color:this.config.baseColor},{position:1,color:i.clamp()}])}return new Pe([{position:0,color:a.clamp()},{position:.5,color:this.config.baseColor},{position:1,color:i.clamp()}])}}Ie.defaultPaletteConfig={baseColor:C("#808080"),steps:11,interpolationMode:Ae.RGB,scaleColorLight:new g(1,1,1,1),scaleColorDark:new g(0,0,0,1),clipLight:.185,clipDark:.16,saturationAdjustmentCutoff:.05,saturationLight:.35,saturationDark:1.25,overlayLight:0,overlayDark:.25,multiplyLight:0,multiplyDark:0,baseScalePosition:.5};Ie.greyscalePaletteConfig={baseColor:C("#808080"),steps:11,interpolationMode:Ae.RGB,scaleColorLight:new g(1,1,1,1),scaleColorDark:new g(0,0,0,1),clipLight:0,clipDark:0,saturationAdjustmentCutoff:0,saturationLight:0,saturationDark:0,overlayLight:0,overlayDark:0,multiplyLight:0,multiplyDark:0,baseScalePosition:.5};function Me(e,t){const o=rgbToHSL(e);let r=Number.MAX_VALUE;let n=0;for(let a=0;a<t.length;a++){const e=rgbToHSL(t[a]);const i=Math.abs(e.l-o.l);if(i<r){r=i;n=a}}return n}function Ge(e,t,o=Ie.greyscalePaletteConfig,r=Ie.defaultPaletteConfig){const n=new Ie(Object.assign(Object.assign({},o),{steps:t}));const a=Me(e,n.palette);return new Ie(Object.assign(Object.assign({},r),{steps:t,baseColor:e,baseScalePosition:a/(t-1)}))}function _e(e,t,o){if(e.length<=1||t<=1){throw new Error("The input array and targetSize must both be greater than 1")}if(o&&t<=e.length){throw new Error("If preserveInputColors is true then targetSize must be greater than the length of the input array")}const r=new Array(e.length);if(o){for(let o=0;o<e.length;o++){const n=o/(e.length-1);let a=2;let i=0;for(let e=0;e<t;e++){const o=Math.abs(e/(t-1)-n);if(o<a){a=o;i=e}if(o===0){break}}r[o]={color:e[o],position:i/(t-1)}}}else{for(let t=0;t<r.length;t++){r[t]={color:e[t],position:t/(e.length-1)}}}const n=new ColorScale(r);const a=new Array(t);for(let i=0;i<t;i++){a[i]=n.getColor(i/(t-1))}return a}const Ee={targetSize:63,spacing:4,scaleColorLight:Ie.defaultPaletteConfig.scaleColorLight,scaleColorDark:Ie.defaultPaletteConfig.scaleColorDark};function qe(e,t=Ee){if(e.length===0){return[]}const o=Math.floor((t.targetSize-((e.length-1)*t.spacing+1))/2);if(o<0){throw new Error("(targetSize - ((input.length - 1) * spacing + 1)) / 2 must be >= 0")}const r=new Array(e.length+2);r[0]={position:0,color:t.scaleColorLight};r[r.length-1]={position:1,color:t.scaleColorDark};for(let i=0;i<e.length;i++){r[i+1]={color:e[i],position:(i*t.spacing+o)/(t.targetSize-1)}}const n=new ColorScale(r);const a=new Array(t.targetSize);for(let i=0;i<t.targetSize;i++){a[i]=n.getColor(i/(t.targetSize-1))}return a}function We(e,t=11,o=Ee){const r=Ge(e,t);const n=qe(r.palette,o);return{short:r.palette,long:n}}class Ue{constructor(e){this.palette=[];this.config=Object.assign({},Ue.defaultPaletteConfig,e);this.regenPalettes()}regenPalettes(){let e=this.config.steps;if(isNaN(e)||e<3){e=3}const t=.14;const o=.06;const r=new g(t,t,t,1);const n=94;const a=new Ie(Object.assign(Object.assign({},Ie.greyscalePaletteConfig),{baseColor:r,baseScalePosition:(1-t)*100/n,steps:e}));const i=a.palette;const l=R(this.config.baseColor);const s=q(this.config.baseColor).l;const c=(l+s)/2;const d=this.matchRelativeLuminanceIndex(c,i);const h=d/(e-1);const u=this.matchRelativeLuminanceIndex(t,i);const p=u/(e-1);const b=q(this.config.baseColor);const f=W(z.fromObject({h:b.h,s:b.s,l:t}));const $=W(z.fromObject({h:b.h,s:b.s,l:o}));const x=new Array(5);x[0]={position:0,color:new g(1,1,1,1)};x[1]={position:h,color:this.config.baseColor};x[2]={position:p,color:f};x[3]={position:.99,color:$};x[4]={position:1,color:new g(0,0,0,1)};const m=new Pe(x);this.palette=new Array(e);for(let g=0;g<e;g++){const t=m.getColor(g/(e-1),Ae.RGB);this.palette[g]=t}}matchRelativeLuminanceIndex(e,t){let o=Number.MAX_VALUE;let r=0;let n=0;const a=t.length;for(;n<a;n++){const a=Math.abs(R(t[n])-e);if(a<o){o=a;r=n}}return r}}Ue.defaultPaletteConfig={baseColor:C("#808080"),steps:94};function Xe(e,t){const o=e.relativeLuminance>t.relativeLuminance?e:t;const r=e.relativeLuminance>t.relativeLuminance?t:e;return(o.relativeLuminance+.05)/(r.relativeLuminance+.05)}const Ze=Object.freeze({create(e,t,o){return new Je(e,t,o)},from(e){return new Je(e.r,e.g,e.b)}});function Ye(e){const t={r:0,g:0,b:0,toColorString:()=>"",contrast:()=>0,relativeLuminance:0};for(const o in t){if(typeof t[o]!==typeof e[o]){return false}}return true}class Je extends g{constructor(e,t,o){super(e,t,o,1);this.toColorString=this.toStringHexRGB;this.contrast=Xe.bind(null,this);this.createCSS=this.toColorString;this.relativeLuminance=P(this)}static fromObject(e){return new Je(e.r,e.g,e.b)}}function Ke(e,t,o=0,r=e.length-1){if(r===o){return e[o]}const n=Math.floor((r-o)/2)+o;return t(e[n])?Ke(e,t,o,n):Ke(e,t,n+1,r)}function Qe(e){return se(e)?-1:1}function et(e,t,o){if(typeof e==="number"){return ot.from(Ze.create(e,t,o))}else{return ot.from(e)}}function tt(e){return Ye(e)?rt.from(e):rt.from(Ze.create(e.r,e.g,e.b))}const ot=Object.freeze({create:et,from:tt});class rt{constructor(e,t){this.closestIndexCache=new Map;this.source=e;this.swatches=t;this.reversedSwatches=Object.freeze([...this.swatches].reverse());this.lastIndex=this.swatches.length-1}colorContrast(e,t,o,r){if(o===undefined){o=this.closestIndexOf(e)}let n=this.swatches;const a=this.lastIndex;let i=o;if(r===undefined){r=Qe(e)}const l=o=>Xe(e,o)>=t;if(r===-1){n=this.reversedSwatches;i=a-i}return Ke(n,l,i,a)}get(e){return this.swatches[e]||this.swatches[r(e,0,this.lastIndex)]}closestIndexOf(e){if(this.closestIndexCache.has(e.relativeLuminance)){return this.closestIndexCache.get(e.relativeLuminance)}let t=this.swatches.indexOf(e);if(t!==-1){this.closestIndexCache.set(e.relativeLuminance,t);return t}const o=this.swatches.reduce(((t,o)=>Math.abs(o.relativeLuminance-e.relativeLuminance)<Math.abs(t.relativeLuminance-e.relativeLuminance)?o:t));t=this.swatches.indexOf(o);this.closestIndexCache.set(e.relativeLuminance,t);return t}static from(e){return new rt(e,Object.freeze(new Ue({baseColor:g.fromObject(e)}).palette.map((e=>{const t=C(e.toStringHexRGB());return Ze.create(t.r,t.g,t.b)}))))}}function nt(e){return Ze.create(e,e,e)}const at={LightMode:1,DarkMode:.23};var it=o(16904);var lt=o(42586);function st(e,t,o,r,n,a,i,l,s){const c=e.source;const d=t.closestIndexOf(o);const h=Math.max(i,l,s);const u=d>=h?-1:1;const p=e.closestIndexOf(c);const g=p;const b=g+u*-1*r;const f=b+u*n;const $=b+u*a;return{rest:e.get(b),hover:e.get(g),active:e.get(f),focus:e.get($)}}function ct(e,t,o,r,n,a,i){const l=e.source;const s=e.closestIndexOf(l);const c=Qe(t);const d=s+(c===1?Math.min(r,n):Math.max(c*r,c*n));const h=e.colorContrast(t,o,d,c);const u=e.closestIndexOf(h);const p=u+c*Math.abs(r-n);const g=c===1?r<n:c*r>c*n;let b;let f;if(g){b=u;f=p}else{b=p;f=u}return{rest:e.get(b),hover:e.get(f),active:e.get(b+c*a),focus:e.get(b+c*i)}}const dt=Ze.create(1,1,1);const ht=Ze.create(0,0,0);const ut=Ze.from(C("#808080"));const pt=Ze.from(C("#DA1A5F"));function gt(e,t){return e.contrast(dt)>=t?dt:ht}function bt(e,t,o,r,n,a){const i=e.closestIndexOf(t);const l=Math.max(o,r,n,a);const s=i>=l?-1:1;return{rest:e.get(i+s*o),hover:e.get(i+s*r),active:e.get(i+s*n),focus:e.get(i+s*a)}}function ft(e,t,o,r,n,a){const i=Qe(t);const l=e.closestIndexOf(t);return{rest:e.get(l-i*o),hover:e.get(l-i*r),active:e.get(l-i*n),focus:e.get(l-i*a)}}function $t(e,t,o){const r=e.closestIndexOf(t);return e.get(r-(r<o?o*-1:o))}function xt(e,t,o,r,n,a,i,l,s,c){const d=Math.max(o,r,n,a,i,l,s,c);const h=e.closestIndexOf(t);const u=h>=d?-1:1;return{rest:e.get(h+u*o),hover:e.get(h+u*r),active:e.get(h+u*n),focus:e.get(h+u*a)}}function mt(e,t,o,r,n,a){const i=Qe(t);const l=e.closestIndexOf(e.colorContrast(t,4.5));const s=l+i*Math.abs(o-r);const c=i===1?o<r:i*o>i*r;let d;let h;if(c){d=l;h=s}else{d=s;h=l}return{rest:e.get(d),hover:e.get(h),active:e.get(d+i*n),focus:e.get(d+i*a)}}function vt(e,t){return e.colorContrast(t,3.5)}function yt(e,t,o){return e.colorContrast(o,3.5,e.closestIndexOf(e.source),Qe(t)*-1)}function wt(e,t){return e.colorContrast(t,14)}function kt(e,t){return e.colorContrast(t,4.5)}function Ft(e,t,o){return e.get(e.closestIndexOf(nt(t))+o)}function Tt(e,t,o){const r=e.closestIndexOf(nt(t))-o;return e.get(r-o)}function Ct(e,t){return e.get(e.closestIndexOf(nt(t)))}function Vt(e,t,o,r,n,a){return Math.max(e.closestIndexOf(nt(t))+o,r,n,a)}function Dt(e,t,o,r,n,a){return e.get(Vt(e,t,o,r,n,a))}function St(e,t,o,r,n,a){return e.get(Vt(e,t,o,r,n,a)+o)}function jt(e,t,o,r,n,a){return e.get(Vt(e,t,o,r,n,a)+o*2)}function Bt(e,t,o,r,n,a){const i=e.closestIndexOf(t);const l=Qe(t);const s=i+l*o;const c=s+l*(r-o);const d=s+l*(n-o);const h=s+l*(a-o);return{rest:e.get(s),hover:e.get(c),active:e.get(d),focus:e.get(h)}}function Ot(e,t,o){return e.get(e.closestIndexOf(t)+Qe(t)*o)}const{create:zt}=it.DesignToken;function Lt(e){return it.DesignToken.create({name:e,cssCustomPropertyName:null})}const Ht=zt("body-font").withDefault('aktiv-grotesk, "Segoe UI", Arial, Helvetica, sans-serif');const Nt=zt("base-height-multiplier").withDefault(10);const At=zt("base-horizontal-spacing-multiplier").withDefault(3);const Rt=zt("base-layer-luminance").withDefault(at.DarkMode);const Pt=zt("control-corner-radius").withDefault(4);const It=zt("density").withDefault(0);const Mt=zt("design-unit").withDefault(4);const Gt=zt("direction").withDefault(lt.N.ltr);const _t=zt("disabled-opacity").withDefault(.3);const Et=zt("stroke-width").withDefault(1);const qt=zt("focus-stroke-width").withDefault(2);const Wt=zt("type-ramp-base-font-size").withDefault("14px");const Ut=zt("type-ramp-base-line-height").withDefault("20px");const Xt=zt("type-ramp-minus-1-font-size").withDefault("12px");const Zt=zt("type-ramp-minus-1-line-height").withDefault("16px");const Yt=zt("type-ramp-minus-2-font-size").withDefault("10px");const Jt=zt("type-ramp-minus-2-line-height").withDefault("16px");const Kt=zt("type-ramp-plus-1-font-size").withDefault("16px");const Qt=zt("type-ramp-plus-1-line-height").withDefault("24px");const eo=zt("type-ramp-plus-2-font-size").withDefault("20px");const to=zt("type-ramp-plus-2-line-height").withDefault("28px");const oo=zt("type-ramp-plus-3-font-size").withDefault("28px");const ro=zt("type-ramp-plus-3-line-height").withDefault("36px");const no=zt("type-ramp-plus-4-font-size").withDefault("34px");const ao=zt("type-ramp-plus-4-line-height").withDefault("44px");const io=zt("type-ramp-plus-5-font-size").withDefault("46px");const lo=zt("type-ramp-plus-5-line-height").withDefault("56px");const so=zt("type-ramp-plus-6-font-size").withDefault("60px");const co=zt("type-ramp-plus-6-line-height").withDefault("72px");const ho=Lt("accent-fill-rest-delta").withDefault(0);const uo=Lt("accent-fill-hover-delta").withDefault(4);const po=Lt("accent-fill-active-delta").withDefault(-5);const go=Lt("accent-fill-focus-delta").withDefault(0);const bo=Lt("accent-foreground-rest-delta").withDefault(0);const fo=Lt("accent-foreground-hover-delta").withDefault(6);const $o=Lt("accent-foreground-active-delta").withDefault(-4);const xo=Lt("accent-foreground-focus-delta").withDefault(0);const mo=Lt("neutral-fill-rest-delta").withDefault(7);const vo=Lt("neutral-fill-hover-delta").withDefault(10);const yo=Lt("neutral-fill-active-delta").withDefault(5);const wo=Lt("neutral-fill-focus-delta").withDefault(0);const ko=Lt("neutral-fill-input-rest-delta").withDefault(0);const Fo=Lt("neutral-fill-input-hover-delta").withDefault(0);const To=Lt("neutral-fill-input-active-delta").withDefault(0);const Co=Lt("neutral-fill-input-focus-delta").withDefault(0);const Vo=Lt("neutral-fill-stealth-rest-delta").withDefault(0);const Do=Lt("neutral-fill-stealth-hover-delta").withDefault(5);const So=Lt("neutral-fill-stealth-active-delta").withDefault(3);const jo=Lt("neutral-fill-stealth-focus-delta").withDefault(0);const Bo=Lt("neutral-fill-strong-rest-delta").withDefault(0);const Oo=Lt("neutral-fill-strong-hover-delta").withDefault(8);const zo=Lt("neutral-fill-strong-active-delta").withDefault(-5);const Lo=Lt("neutral-fill-strong-focus-delta").withDefault(0);const Ho=Lt("neutral-fill-layer-rest-delta").withDefault(3);const No=Lt("neutral-stroke-rest-delta").withDefault(25);const Ao=Lt("neutral-stroke-hover-delta").withDefault(40);const Ro=Lt("neutral-stroke-active-delta").withDefault(16);const Po=Lt("neutral-stroke-focus-delta").withDefault(25);const Io=Lt("neutral-stroke-divider-rest-delta").withDefault(8);const Mo=zt("neutral-color").withDefault(ut);const Go=Lt("neutral-palette").withDefault((e=>ot.from(Mo.getValueFor(e))));const _o=zt("accent-color").withDefault(pt);const Eo=Lt("accent-palette").withDefault((e=>ot.from(_o.getValueFor(e))));const qo=Lt("neutral-layer-card-container-recipe").withDefault({evaluate:e=>Ft(Go.getValueFor(e),Rt.getValueFor(e),Ho.getValueFor(e))});const Wo=zt("neutral-layer-card-container").withDefault((e=>qo.getValueFor(e).evaluate(e)));const Uo=Lt("neutral-layer-floating-recipe").withDefault({evaluate:e=>Tt(Go.getValueFor(e),Rt.getValueFor(e),Ho.getValueFor(e))});const Xo=zt("neutral-layer-floating").withDefault((e=>Uo.getValueFor(e).evaluate(e)));const Zo=Lt("neutral-layer-1-recipe").withDefault({evaluate:e=>Ct(Go.getValueFor(e),Rt.getValueFor(e))});const Yo=zt("neutral-layer-1").withDefault((e=>Zo.getValueFor(e).evaluate(e)));const Jo=Lt("neutral-layer-2-recipe").withDefault({evaluate:e=>Dt(Go.getValueFor(e),Rt.getValueFor(e),Ho.getValueFor(e),mo.getValueFor(e),vo.getValueFor(e),yo.getValueFor(e))});const Ko=zt("neutral-layer-2").withDefault((e=>Jo.getValueFor(e).evaluate(e)));const Qo=Lt("neutral-layer-3-recipe").withDefault({evaluate:e=>St(Go.getValueFor(e),Rt.getValueFor(e),Ho.getValueFor(e),mo.getValueFor(e),vo.getValueFor(e),yo.getValueFor(e))});const er=zt("neutral-layer-3").withDefault((e=>Qo.getValueFor(e).evaluate(e)));const tr=Lt("neutral-layer-4-recipe").withDefault({evaluate:e=>jt(Go.getValueFor(e),Rt.getValueFor(e),Ho.getValueFor(e),mo.getValueFor(e),vo.getValueFor(e),yo.getValueFor(e))});const or=zt("neutral-layer-4").withDefault((e=>tr.getValueFor(e).evaluate(e)));const rr=zt("fill-color").withDefault((e=>Yo.getValueFor(e)));var nr;(function(e){e[e["normal"]=4.5]="normal";e[e["large"]=7]="large"})(nr||(nr={}));const ar=zt({name:"accent-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>st(Eo.getValueFor(e),Go.getValueFor(e),t||rr.getValueFor(e),uo.getValueFor(e),po.getValueFor(e),go.getValueFor(e),mo.getValueFor(e),vo.getValueFor(e),yo.getValueFor(e))});const ir=zt("accent-fill-rest").withDefault((e=>ar.getValueFor(e).evaluate(e).rest));const lr=zt("accent-fill-hover").withDefault((e=>ar.getValueFor(e).evaluate(e).hover));const sr=zt("accent-fill-active").withDefault((e=>ar.getValueFor(e).evaluate(e).active));const cr=zt("accent-fill-focus").withDefault((e=>ar.getValueFor(e).evaluate(e).focus));const dr=e=>(t,o)=>gt(o||ir.getValueFor(t),e);const hr=Lt("foreground-on-accent-recipe").withDefault({evaluate:(e,t)=>dr(nr.normal)(e,t)});const ur=zt("foreground-on-accent-rest").withDefault((e=>hr.getValueFor(e).evaluate(e,ir.getValueFor(e))));const pr=zt("foreground-on-accent-hover").withDefault((e=>hr.getValueFor(e).evaluate(e,lr.getValueFor(e))));const gr=zt("foreground-on-accent-active").withDefault((e=>hr.getValueFor(e).evaluate(e,sr.getValueFor(e))));const br=zt("foreground-on-accent-focus").withDefault((e=>hr.getValueFor(e).evaluate(e,cr.getValueFor(e))));const fr=Lt("foreground-on-accent-large-recipe").withDefault({evaluate:(e,t)=>dr(nr.large)(e,t)});const $r=zt("foreground-on-accent-rest-large").withDefault((e=>fr.getValueFor(e).evaluate(e,ir.getValueFor(e))));const xr=zt("foreground-on-accent-hover-large").withDefault((e=>fr.getValueFor(e).evaluate(e,lr.getValueFor(e))));const mr=zt("foreground-on-accent-active-large").withDefault((e=>fr.getValueFor(e).evaluate(e,sr.getValueFor(e))));const vr=zt("foreground-on-accent-focus-large").withDefault((e=>fr.getValueFor(e).evaluate(e,cr.getValueFor(e))));const yr=e=>(t,o)=>ct(Eo.getValueFor(t),o||rr.getValueFor(t),e,bo.getValueFor(t),fo.getValueFor(t),$o.getValueFor(t),xo.getValueFor(t));const wr=zt({name:"accent-foreground-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>yr(nr.normal)(e,t)});const kr=zt("accent-foreground-rest").withDefault((e=>wr.getValueFor(e).evaluate(e).rest));const Fr=zt("accent-foreground-hover").withDefault((e=>wr.getValueFor(e).evaluate(e).hover));const Tr=zt("accent-foreground-active").withDefault((e=>wr.getValueFor(e).evaluate(e).active));const Cr=zt("accent-foreground-focus").withDefault((e=>wr.getValueFor(e).evaluate(e).focus));const Vr=zt({name:"neutral-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>bt(Go.getValueFor(e),t||rr.getValueFor(e),mo.getValueFor(e),vo.getValueFor(e),yo.getValueFor(e),wo.getValueFor(e))});const Dr=zt("neutral-fill-rest").withDefault((e=>Vr.getValueFor(e).evaluate(e).rest));const Sr=zt("neutral-fill-hover").withDefault((e=>Vr.getValueFor(e).evaluate(e).hover));const jr=zt("neutral-fill-active").withDefault((e=>Vr.getValueFor(e).evaluate(e).active));const Br=zt("neutral-fill-focus").withDefault((e=>Vr.getValueFor(e).evaluate(e).focus));const Or=zt({name:"neutral-fill-input-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>ft(Go.getValueFor(e),t||rr.getValueFor(e),ko.getValueFor(e),Fo.getValueFor(e),To.getValueFor(e),Co.getValueFor(e))});const zr=zt("neutral-fill-input-rest").withDefault((e=>Or.getValueFor(e).evaluate(e).rest));const Lr=zt("neutral-fill-input-hover").withDefault((e=>Or.getValueFor(e).evaluate(e).hover));const Hr=zt("neutral-fill-input-active").withDefault((e=>Or.getValueFor(e).evaluate(e).active));const Nr=zt("neutral-fill-input-focus").withDefault((e=>Or.getValueFor(e).evaluate(e).focus));const Ar=zt({name:"neutral-fill-stealth-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>xt(Go.getValueFor(e),t||rr.getValueFor(e),Vo.getValueFor(e),Do.getValueFor(e),So.getValueFor(e),jo.getValueFor(e),mo.getValueFor(e),vo.getValueFor(e),yo.getValueFor(e),wo.getValueFor(e))});const Rr=zt("neutral-fill-stealth-rest").withDefault((e=>Ar.getValueFor(e).evaluate(e).rest));const Pr=zt("neutral-fill-stealth-hover").withDefault((e=>Ar.getValueFor(e).evaluate(e).hover));const Ir=zt("neutral-fill-stealth-active").withDefault((e=>Ar.getValueFor(e).evaluate(e).active));const Mr=zt("neutral-fill-stealth-focus").withDefault((e=>Ar.getValueFor(e).evaluate(e).focus));const Gr=zt({name:"neutral-fill-strong-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>mt(Go.getValueFor(e),t||rr.getValueFor(e),Bo.getValueFor(e),Oo.getValueFor(e),zo.getValueFor(e),Lo.getValueFor(e))});const _r=zt("neutral-fill-strong-rest").withDefault((e=>Gr.getValueFor(e).evaluate(e).rest));const Er=zt("neutral-fill-strong-hover").withDefault((e=>Gr.getValueFor(e).evaluate(e).hover));const qr=zt("neutral-fill-strong-active").withDefault((e=>Gr.getValueFor(e).evaluate(e).active));const Wr=zt("neutral-fill-strong-focus").withDefault((e=>Gr.getValueFor(e).evaluate(e).focus));const Ur=Lt("neutral-fill-layer-recipe").withDefault({evaluate:(e,t)=>$t(Go.getValueFor(e),t||rr.getValueFor(e),Ho.getValueFor(e))});const Xr=zt("neutral-fill-layer-rest").withDefault((e=>Ur.getValueFor(e).evaluate(e)));const Zr=Lt("focus-stroke-outer-recipe").withDefault({evaluate:e=>vt(Go.getValueFor(e),rr.getValueFor(e))});const Yr=zt("focus-stroke-outer").withDefault((e=>Zr.getValueFor(e).evaluate(e)));const Jr=Lt("focus-stroke-inner-recipe").withDefault({evaluate:e=>yt(Eo.getValueFor(e),rr.getValueFor(e),Yr.getValueFor(e))});const Kr=zt("focus-stroke-inner").withDefault((e=>Jr.getValueFor(e).evaluate(e)));const Qr=Lt("neutral-foreground-hint-recipe").withDefault({evaluate:e=>kt(Go.getValueFor(e),rr.getValueFor(e))});const en=zt("neutral-foreground-hint").withDefault((e=>Qr.getValueFor(e).evaluate(e)));const tn=Lt("neutral-foreground-recipe").withDefault({evaluate:e=>wt(Go.getValueFor(e),rr.getValueFor(e))});const on=zt("neutral-foreground-rest").withDefault((e=>tn.getValueFor(e).evaluate(e)));const rn=zt({name:"neutral-stroke-recipe",cssCustomPropertyName:null}).withDefault({evaluate:e=>Bt(Go.getValueFor(e),rr.getValueFor(e),No.getValueFor(e),Ao.getValueFor(e),Ro.getValueFor(e),Po.getValueFor(e))});const nn=zt("neutral-stroke-rest").withDefault((e=>rn.getValueFor(e).evaluate(e).rest));const an=zt("neutral-stroke-hover").withDefault((e=>rn.getValueFor(e).evaluate(e).hover));const ln=zt("neutral-stroke-active").withDefault((e=>rn.getValueFor(e).evaluate(e).active));const sn=zt("neutral-stroke-focus").withDefault((e=>rn.getValueFor(e).evaluate(e).focus));const cn=Lt("neutral-stroke-divider-recipe").withDefault({evaluate:(e,t)=>Ot(Go.getValueFor(e),t||rr.getValueFor(e),Io.getValueFor(e))});const dn=zt("neutral-stroke-divider-rest").withDefault((e=>cn.getValueFor(e).evaluate(e)));const hn=it.DesignToken.create({name:"height-number",cssCustomPropertyName:null}).withDefault((e=>(Nt.getValueFor(e)+It.getValueFor(e))*Mt.getValueFor(e)));const un="data-jp-theme-name";const pn="data-jp-theme-light";const gn="--jp-layout-color1";let bn=false;function fn(){if(!bn){bn=true;$n()}}function $n(){const e=()=>{const e=new MutationObserver((()=>{vn()}));e.observe(document.body,{attributes:true,attributeFilter:[un],childList:false,characterData:false});vn()};if(document.readyState==="complete"){e()}else{window.addEventListener("load",e)}}const xn=e=>{const t=parseInt(e,10);return isNaN(t)?null:t};const mn={"--jp-border-width":{converter:xn,token:Et},"--jp-border-radius":{converter:xn,token:Pt},[gn]:{converter:(e,t)=>{const o=O(e);if(o){const e=q(o);const t=z.fromObject({h:e.h,s:e.s,l:.5});const r=W(t);return ot.from(Ze.create(r.r,r.g,r.b))}else{return null}},token:Go},"--jp-brand-color1":{converter:(e,t)=>{const o=O(e);if(o){const e=q(o);const r=t?1:-1;const n=z.fromObject({h:e.h,s:e.s,l:e.l+r*uo.getValueFor(document.body)/94});const a=W(n);return ot.from(Ze.create(a.r,a.g,a.b))}else{return null}},token:Eo},"--jp-ui-font-family":{token:Ht},"--jp-ui-font-size1":{token:Wt}};function vn(){var e;const t=getComputedStyle(document.body);const o=document.body.getAttribute(pn);let r=false;if(o){r=o==="false"}else{const e=t.getPropertyValue(gn).toString();if(e){const t=O(e);if(t){r=se(Ze.create(t.r,t.g,t.b));console.debug(`Theme is ${r?"dark":"light"} based on '${gn}' value: ${e}.`)}}}Rt.setValueFor(document.body,r?at.DarkMode:at.LightMode);for(const n in mn){const o=mn[n];const a=t.getPropertyValue(n).toString();if(document.body&&a!==""){const t=((e=o.converter)!==null&&e!==void 0?e:e=>e)(a.trim(),r);if(t!==null){o.token.setValueFor(document.body,t)}else{console.error(`Fail to parse value '${a}' for '${n}' as FAST design token.`)}}}}const yn=Ze.create(1,1,1);const wn=Ze.create(0,0,0);const kn=C("#D32F2F");var Fn;(function(e){e[e["normal"]=4.5]="normal";e[e["large"]=7]="large"})(Fn||(Fn={}));function Tn(e,t,o,r,n,a,i,l,s){const c=e.source;const d=t.closestIndexOf(o);const h=Math.max(i,l,s);const u=d>=h?-1:1;const p=e.closestIndexOf(c);const g=p;const b=g+u*-1*r;const f=b+u*n;const $=b+u*a;return{rest:e.get(b),hover:e.get(g),active:e.get(f),focus:e.get($)}}function Cn(e,t,o,r,n,a,i){const l=e.source;const s=e.closestIndexOf(l);const c=se(t)?-1:1;const d=s+(c===1?Math.min(r,n):Math.max(c*r,c*n));const h=e.colorContrast(t,o,d,c);const u=e.closestIndexOf(h);const p=u+c*Math.abs(r-n);const g=c===1?r<n:c*r>c*n;let b;let f;if(g){b=u;f=p}else{b=p;f=u}return{rest:e.get(b),hover:e.get(f),active:e.get(b+c*a),focus:e.get(b+c*i)}}function Vn(e,t){return e.contrast(yn)>=t?yn:wn}const Dn=Ze.create(kn.r,kn.g,kn.b);class Sn{constructor(e,t){this.cache=new WeakMap;this.ltr=e;this.rtl=t}bind(e){this.attach(e)}unbind(e){const t=this.cache.get(e);if(t){Gt.unsubscribe(t)}}attach(e){const t=this.cache.get(e)||new jn(this.ltr,this.rtl,e);const o=Gt.getValueFor(e);Gt.subscribe(t);t.attach(o);this.cache.set(e,t)}}class jn{constructor(e,t,o){this.ltr=e;this.rtl=t;this.source=o;this.attached=null}handleChange({target:e,token:t}){this.attach(t.getValueFor(e))}attach(e){if(this.attached!==this[e]){if(this.attached!==null){this.source.$fastController.removeStyles(this.attached)}this.attached=this[e];if(this.attached!==null){this.source.$fastController.addStyles(this.attached)}}}}const{create:Bn}=it.DesignToken;const On=Bn({name:"error-palette",cssCustomPropertyName:null}).withDefault(ot.from(Dn));const zn=Bn({name:"error-fill-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>Tn(On.getValueFor(e),Go.getValueFor(e),t||rr.getValueFor(e),uo.getValueFor(e),po.getValueFor(e),go.getValueFor(e),mo.getValueFor(e),vo.getValueFor(e),yo.getValueFor(e))});const Ln=Bn("error-fill-rest").withDefault((e=>zn.getValueFor(e).evaluate(e).rest));const Hn=Bn("error-fill-hover").withDefault((e=>zn.getValueFor(e).evaluate(e).hover));const Nn=Bn("error-fill-active").withDefault((e=>zn.getValueFor(e).evaluate(e).active));const An=Bn("error-fill-focus").withDefault((e=>zn.getValueFor(e).evaluate(e).focus));const Rn=e=>(t,o)=>Vn(o||Ln.getValueFor(t),e);const Pn=Bn({name:"foreground-on-error-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>Rn(Fn.normal)(e,t)});const In=Bn("foreground-on-error-rest").withDefault((e=>Pn.getValueFor(e).evaluate(e,Ln.getValueFor(e))));const Mn=Bn("foreground-on-error-hover").withDefault((e=>Pn.getValueFor(e).evaluate(e,Hn.getValueFor(e))));const Gn=Bn("foreground-on-error-active").withDefault((e=>Pn.getValueFor(e).evaluate(e,Nn.getValueFor(e))));const _n=Bn("foreground-on-error-focus").withDefault((e=>Pn.getValueFor(e).evaluate(e,An.getValueFor(e))));const En=Bn({name:"foreground-on-error-large-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>Rn(Fn.large)(e,t)});const qn=Bn("foreground-on-error-rest-large").withDefault((e=>En.getValueFor(e).evaluate(e,Ln.getValueFor(e))));const Wn=Bn("foreground-on-error-hover-large").withDefault((e=>En.getValueFor(e).evaluate(e,Hn.getValueFor(e))));const Un=Bn("foreground-on-error-active-large").withDefault((e=>En.getValueFor(e).evaluate(e,Nn.getValueFor(e))));const Xn=Bn("foreground-on-error-focus-large").withDefault((e=>En.getValueFor(e).evaluate(e,An.getValueFor(e))));const Zn=e=>(t,o)=>Cn(On.getValueFor(t),o||rr.getValueFor(t),e,bo.getValueFor(t),fo.getValueFor(t),$o.getValueFor(t),xo.getValueFor(t));const Yn=Bn({name:"error-foreground-recipe",cssCustomPropertyName:null}).withDefault({evaluate:(e,t)=>Zn(Fn.normal)(e,t)});const Jn=Bn("error-foreground-rest").withDefault((e=>Yn.getValueFor(e).evaluate(e).rest));const Kn=Bn("error-foreground-hover").withDefault((e=>Yn.getValueFor(e).evaluate(e).hover));const Qn=Bn("error-foreground-active").withDefault((e=>Yn.getValueFor(e).evaluate(e).active));const ea=Bn("error-foreground-focus").withDefault((e=>Yn.getValueFor(e).evaluate(e).focus));function ta(e){return it.DesignSystem.getOrCreate(e).withPrefix("jp")}var oa=o(81351);const ra=(e,t)=>oa.css`
        ${(0,it.display)("flex")} :host {
            box-sizing: border-box;
            flex-direction: column;
            font-family: ${Ht};
            font-size: ${Xt};
            line-height: ${Zt};
            color: ${on};
            border-top: calc(${Et} * 1px) solid ${dn};
        }
    `;var na;(function(e){e["Canvas"]="Canvas";e["CanvasText"]="CanvasText";e["LinkText"]="LinkText";e["VisitedText"]="VisitedText";e["ActiveText"]="ActiveText";e["ButtonFace"]="ButtonFace";e["ButtonText"]="ButtonText";e["Field"]="Field";e["FieldText"]="FieldText";e["Highlight"]="Highlight";e["HighlightText"]="HighlightText";e["GrayText"]="GrayText"})(na||(na={}));const aa=oa.cssPartial`(${Nt} + ${It}) * ${Mt}`;const ia=(e,t)=>oa.css`
    ${(0,it.display)("flex")} :host {
      box-sizing: border-box;
      font-family: ${Ht};
      flex-direction: column;
      font-size: ${Xt};
      line-height: ${Zt};
      border-bottom: calc(${Et} * 1px) solid
        ${dn};
    }

    .region {
      display: none;
      padding: calc((6 + (${Mt} * 2 * ${It})) * 1px);
    }

    div.heading {
      display: grid;
      position: relative;
      grid-template-columns: calc(${aa} * 1px) auto 1fr auto;
      color: ${on};
    }

    .button {
      appearance: none;
      border: none;
      background: none;
      grid-column: 3;
      outline: none;
      padding: 0 calc((6 + (${Mt} * 2 * ${It})) * 1px);
      text-align: left;
      height: calc(${aa} * 1px);
      color: currentcolor;
      cursor: pointer;
      font-family: inherit;
    }

    .button:hover {
      color: currentcolor;
    }

    .button:active {
      color: currentcolor;
    }

    .button::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      cursor: pointer;
    }

    /* prettier-ignore */
    .button:${it.focusVisible}::before {
      outline: none;
      border: calc(${qt} * 1px) solid ${cr};
      border-radius: calc(${Pt} * 1px);
    }

    :host([expanded]) .region {
      display: block;
    }

    .icon {
      display: flex;
      align-items: center;
      justify-content: center;
      grid-column: 1;
      grid-row: 1;
      pointer-events: none;
      position: relative;
    }

    slot[name='expanded-icon'],
    slot[name='collapsed-icon'] {
      fill: currentcolor;
    }

    slot[name='collapsed-icon'] {
      display: flex;
    }

    :host([expanded]) slot[name='collapsed-icon'] {
      display: none;
    }

    slot[name='expanded-icon'] {
      display: none;
    }

    :host([expanded]) slot[name='expanded-icon'] {
      display: flex;
    }

    .start {
      display: flex;
      align-items: center;
      padding-inline-start: calc(${Mt} * 1px);
      justify-content: center;
      grid-column: 2;
      position: relative;
    }

    .end {
      display: flex;
      align-items: center;
      justify-content: center;
      grid-column: 4;
      position: relative;
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      /* prettier-ignore */
      .button:${it.focusVisible}::before {
          border-color: ${na.Highlight};
        }
      :host slot[name='collapsed-icon'],
      :host([expanded]) slot[name='expanded-icon'] {
        fill: ${na.ButtonText};
      }
    `));const la=it.AccordionItem.compose({baseName:"accordion-item",template:it.accordionItemTemplate,styles:ia,collapsedIcon:`\n      <svg\n        width="20"\n        height="20"\n        viewBox="0 0 16 16"\n        xmlns="http://www.w3.org/2000/svg"\n        class="expand-collapse-glyph"\n      >\n        <path\n          fill-rule="evenodd"\n          clip-rule="evenodd"\n          d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"\n        />\n      </svg>\n    `,expandedIcon:`\n      <svg\n        width="20"\n        height="20"\n        viewBox="0 0 16 16"\n        xmlns="http://www.w3.org/2000/svg"\n        class="expand-collapse-glyph"\n      >\n        <path\n          fill-rule="evenodd"\n          clip-rule="evenodd"\n          transform="rotate(90,8,8)"\n          d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"\n        />\n      </svg>\n    `});const sa=it.Accordion.compose({baseName:"accordion",template:it.accordionTemplate,styles:ra});var ca=function(e,t){ca=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var o in t)if(t.hasOwnProperty(o))e[o]=t[o]};return ca(e,t)};function da(e,t){ca(e,t);function o(){this.constructor=e}e.prototype=t===null?Object.create(t):(o.prototype=t.prototype,new o)}var ha=function(){ha=Object.assign||function e(t){for(var o,r=1,n=arguments.length;r<n;r++){o=arguments[r];for(var a in o)if(Object.prototype.hasOwnProperty.call(o,a))t[a]=o[a]}return t};return ha.apply(this,arguments)};function ua(e,t){var o={};for(var r in e)if(Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0)o[r]=e[r];if(e!=null&&typeof Object.getOwnPropertySymbols==="function")for(var n=0,r=Object.getOwnPropertySymbols(e);n<r.length;n++){if(t.indexOf(r[n])<0&&Object.prototype.propertyIsEnumerable.call(e,r[n]))o[r[n]]=e[r[n]]}return o}function pa(e,t,o,r){var n=arguments.length,a=n<3?t:r===null?r=Object.getOwnPropertyDescriptor(t,o):r,i;if(typeof Reflect==="object"&&typeof Reflect.decorate==="function")a=Reflect.decorate(e,t,o,r);else for(var l=e.length-1;l>=0;l--)if(i=e[l])a=(n<3?i(a):n>3?i(t,o,a):i(t,o))||a;return n>3&&a&&Object.defineProperty(t,o,a),a}function ga(e,t){return function(o,r){t(o,r,e)}}function ba(e,t){if(typeof Reflect==="object"&&typeof Reflect.metadata==="function")return Reflect.metadata(e,t)}function fa(e,t,o,r){function n(e){return e instanceof o?e:new o((function(t){t(e)}))}return new(o||(o=Promise))((function(o,a){function i(e){try{s(r.next(e))}catch(t){a(t)}}function l(e){try{s(r["throw"](e))}catch(t){a(t)}}function s(e){e.done?o(e.value):n(e.value).then(i,l)}s((r=r.apply(e,t||[])).next())}))}function $a(e,t){var o={label:0,sent:function(){if(a[0]&1)throw a[1];return a[1]},trys:[],ops:[]},r,n,a,i;return i={next:l(0),throw:l(1),return:l(2)},typeof Symbol==="function"&&(i[Symbol.iterator]=function(){return this}),i;function l(e){return function(t){return s([e,t])}}function s(i){if(r)throw new TypeError("Generator is already executing.");while(o)try{if(r=1,n&&(a=i[0]&2?n["return"]:i[0]?n["throw"]||((a=n["return"])&&a.call(n),0):n.next)&&!(a=a.call(n,i[1])).done)return a;if(n=0,a)i=[i[0]&2,a.value];switch(i[0]){case 0:case 1:a=i;break;case 4:o.label++;return{value:i[1],done:false};case 5:o.label++;n=i[1];i=[0];continue;case 7:i=o.ops.pop();o.trys.pop();continue;default:if(!(a=o.trys,a=a.length>0&&a[a.length-1])&&(i[0]===6||i[0]===2)){o=0;continue}if(i[0]===3&&(!a||i[1]>a[0]&&i[1]<a[3])){o.label=i[1];break}if(i[0]===6&&o.label<a[1]){o.label=a[1];a=i;break}if(a&&o.label<a[2]){o.label=a[2];o.ops.push(i);break}if(a[2])o.ops.pop();o.trys.pop();continue}i=t.call(e,o)}catch(l){i=[6,l];n=0}finally{r=a=0}if(i[0]&5)throw i[1];return{value:i[0]?i[1]:void 0,done:true}}}function xa(e,t,o,r){if(r===undefined)r=o;e[r]=t[o]}function ma(e,t){for(var o in e)if(o!=="default"&&!t.hasOwnProperty(o))t[o]=e[o]}function va(e){var t=typeof Symbol==="function"&&Symbol.iterator,o=t&&e[t],r=0;if(o)return o.call(e);if(e&&typeof e.length==="number")return{next:function(){if(e&&r>=e.length)e=void 0;return{value:e&&e[r++],done:!e}}};throw new TypeError(t?"Object is not iterable.":"Symbol.iterator is not defined.")}function ya(e,t){var o=typeof Symbol==="function"&&e[Symbol.iterator];if(!o)return e;var r=o.call(e),n,a=[],i;try{while((t===void 0||t-- >0)&&!(n=r.next()).done)a.push(n.value)}catch(l){i={error:l}}finally{try{if(n&&!n.done&&(o=r["return"]))o.call(r)}finally{if(i)throw i.error}}return a}function wa(){for(var e=[],t=0;t<arguments.length;t++)e=e.concat(ya(arguments[t]));return e}function ka(){for(var e=0,t=0,o=arguments.length;t<o;t++)e+=arguments[t].length;for(var r=Array(e),n=0,t=0;t<o;t++)for(var a=arguments[t],i=0,l=a.length;i<l;i++,n++)r[n]=a[i];return r}function Fa(e){return this instanceof Fa?(this.v=e,this):new Fa(e)}function Ta(e,t,o){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var r=o.apply(e,t||[]),n,a=[];return n={},i("next"),i("throw"),i("return"),n[Symbol.asyncIterator]=function(){return this},n;function i(e){if(r[e])n[e]=function(t){return new Promise((function(o,r){a.push([e,t,o,r])>1||l(e,t)}))}}function l(e,t){try{s(r[e](t))}catch(o){h(a[0][3],o)}}function s(e){e.value instanceof Fa?Promise.resolve(e.value.v).then(c,d):h(a[0][2],e)}function c(e){l("next",e)}function d(e){l("throw",e)}function h(e,t){if(e(t),a.shift(),a.length)l(a[0][0],a[0][1])}}function Ca(e){var t,o;return t={},r("next"),r("throw",(function(e){throw e})),r("return"),t[Symbol.iterator]=function(){return this},t;function r(r,n){t[r]=e[r]?function(t){return(o=!o)?{value:Fa(e[r](t)),done:r==="return"}:n?n(t):t}:n}}function Va(e){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var t=e[Symbol.asyncIterator],o;return t?t.call(e):(e=typeof va==="function"?va(e):e[Symbol.iterator](),o={},r("next"),r("throw"),r("return"),o[Symbol.asyncIterator]=function(){return this},o);function r(t){o[t]=e[t]&&function(o){return new Promise((function(r,a){o=e[t](o),n(r,a,o.done,o.value)}))}}function n(e,t,o,r){Promise.resolve(r).then((function(t){e({value:t,done:o})}),t)}}function Da(e,t){if(Object.defineProperty){Object.defineProperty(e,"raw",{value:t})}else{e.raw=t}return e}function Sa(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var o in e)if(Object.hasOwnProperty.call(e,o))t[o]=e[o];t.default=e;return t}function ja(e){return e&&e.__esModule?e:{default:e}}function Ba(e,t){if(!t.has(e)){throw new TypeError("attempted to get private field on non-instance")}return t.get(e)}function Oa(e,t,o){if(!t.has(e)){throw new TypeError("attempted to set private field on non-instance")}t.set(e,o);return o}var za;(function(e){e["Canvas"]="Canvas";e["CanvasText"]="CanvasText";e["LinkText"]="LinkText";e["VisitedText"]="VisitedText";e["ActiveText"]="ActiveText";e["ButtonFace"]="ButtonFace";e["ButtonText"]="ButtonText";e["Field"]="Field";e["FieldText"]="FieldText";e["Highlight"]="Highlight";e["HighlightText"]="HighlightText";e["GrayText"]="GrayText"})(za||(za={}));const La=oa.cssPartial`(${Nt} + ${It}) * ${Mt}`;const Ha=oa.css`
    ${(0,it.display)("inline-flex")} :host {
        font-family: ${Ht};
        outline: none;
        font-size: ${Wt};
        line-height: ${Ut};
        height: calc(${La} * 1px);
        min-width: calc(${La} * 1px);
        background-color: ${Dr};
        color: ${on};
        border-radius: calc(${Pt} * 1px);
        fill: currentcolor;
        cursor: pointer;
    }

    .control {
        background: transparent;
        height: inherit;
        flex-grow: 1;
        box-sizing: border-box;
        display: inline-flex;
        justify-content: center;
        align-items: baseline;
        padding: 0 calc((10 + (${Mt} * 2 * ${It})) * 1px);
        white-space: nowrap;
        outline: none;
        text-decoration: none;
        border: calc(${Et} * 1px) solid transparent;
        color: inherit;
        border-radius: inherit;
        fill: inherit;
        cursor: inherit;
        font-weight: inherit;
        font-family: inherit;
        font-size: inherit;
        line-height: inherit;
    }

    :host(:hover) {
        background-color: ${Sr};
    }

    :host(:active) {
        background-color: ${jr};
    }

    .control:${it.focusVisible} {
        border-color: ${Yr};
        box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px) ${Yr} inset;
    }

    .control::-moz-focus-inner {
        border: 0;
    }

    .start,
    .content,
    .end {
        align-self: center;
    }

    .start,
    .end {
        display: flex;
    }

    .control.icon-only {
        padding: 0;
        line-height: 0;
    }

    ::slotted(svg) {
        ${""} width: 16px;
        height: 16px;
        pointer-events: none;
    }

    .start {
        margin-inline-end: 11px;
    }

    .end {
        margin-inline-start: 11px;
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
            :host .control {
              background-color: ${za.ButtonFace};
              border-color: ${za.ButtonText};
              color: ${za.ButtonText};
              fill: currentColor;
            }

            :host(:hover) .control {
              forced-color-adjust: none;
              background-color: ${za.Highlight};
              color: ${za.HighlightText};
            }

            .control:${it.focusVisible} {
              forced-color-adjust: none;
              background-color: ${za.Highlight};
              border-color: ${za.ButtonText};
              box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px) ${za.ButtonText} inset;
              color: ${za.HighlightText};
            }

            .control:hover,
            :host([appearance="outline"]) .control:hover {
              border-color: ${za.ButtonText};
            }

            :host([href]) .control {
                border-color: ${za.LinkText};
                color: ${za.LinkText};
            }

            :host([href]) .control:hover,
            :host([href]) .control:${it.focusVisible}{
              forced-color-adjust: none;
              background: ${za.ButtonFace};
              border-color: ${za.LinkText};
              box-shadow: 0 0 0 1px ${za.LinkText} inset;
              color: ${za.LinkText};
              fill: currentColor;
            }
        `));const Na=oa.css`
    :host([appearance="accent"]) {
        background: ${ir};
        color: ${ur};
    }

    :host([appearance="accent"]:hover) {
        background: ${lr};
        color: ${pr};
    }

    :host([appearance="accent"]:active) .control:active {
        background: ${sr};
        color: ${gr};
    }

    :host([appearance="accent"]) .control:${it.focusVisible} {
        box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px) ${Yr} inset,
            0 0 0 calc((${qt} + ${Et}) * 1px) ${Kr} inset;
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
            :host([appearance="accent"]) .control {
                forced-color-adjust: none;
                background: ${za.Highlight};
                color: ${za.HighlightText};
            }

            :host([appearance="accent"]) .control:hover,
            :host([appearance="accent"]:active) .control:active {
                background: ${za.HighlightText};
                border-color: ${za.Highlight};
                color: ${za.Highlight};
            }

            :host([appearance="accent"]) .control:${it.focusVisible} {
                border-color: ${za.Highlight};
                box-shadow: 0 0 0 calc(${qt} * 1px) ${za.HighlightText} inset;
            }

            :host([appearance="accent"][href]) .control{
                background: ${za.LinkText};
                color: ${za.HighlightText};
            }

            :host([appearance="accent"][href]) .control:hover {
                background: ${za.ButtonFace};
                border-color: ${za.LinkText};
                box-shadow: none;
                color: ${za.LinkText};
                fill: currentColor;
            }

            :host([appearance="accent"][href]) .control:${it.focusVisible} {
                border-color: ${za.LinkText};
                box-shadow: 0 0 0 calc(${qt} * 1px) ${za.HighlightText} inset;
            }
        `));const Aa=oa.css`
    :host([appearance="hypertext"]) {
        font-size: inherit;
        line-height: inherit;
        height: auto;
        min-width: 0;
        background: transparent;
    }

    :host([appearance="hypertext"]) .control {
        display: inline;
        padding: 0;
        border: none;
        box-shadow: none;
        border-radius: 0;
        line-height: 1;
    }

    :host a.control:not(:link) {
        background-color: transparent;
        cursor: default;
    }
    :host([appearance="hypertext"]) .control:link,
    :host([appearance="hypertext"]) .control:visited {
        background: transparent;
        color: ${kr};
        border-bottom: calc(${Et} * 1px) solid ${kr};
    }

    :host([appearance="hypertext"]:hover),
    :host([appearance="hypertext"]) .control:hover {
        background: transparent;
        border-bottom-color: ${Fr};
    }

    :host([appearance="hypertext"]:active),
    :host([appearance="hypertext"]) .control:active {
        background: transparent;
        border-bottom-color: ${Tr};
    }

    :host([appearance="hypertext"]) .control:${it.focusVisible} {
        border-bottom: calc(${qt} * 1px) solid ${Yr};
        margin-bottom: calc(calc(${Et} - ${qt}) * 1px);
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
            :host([appearance="hypertext"]:hover) {
                background-color: ${za.ButtonFace};
                color: ${za.ButtonText};
            }
            :host([appearance="hypertext"][href]) .control:hover,
            :host([appearance="hypertext"][href]) .control:active,
            :host([appearance="hypertext"][href]) .control:${it.focusVisible} {
                color: ${za.LinkText};
                border-bottom-color: ${za.LinkText};
                box-shadow: none;
            }
        `));const Ra=oa.css`
    :host([appearance="lightweight"]) {
        background: transparent;
        color: ${kr};
    }

    :host([appearance="lightweight"]) .control {
        padding: 0;
        height: initial;
        border: none;
        box-shadow: none;
        border-radius: 0;
    }

    :host([appearance="lightweight"]:hover) {
        background: transparent;
        color: ${Fr};
    }

    :host([appearance="lightweight"]:active) {
        background: transparent;
        color: ${Tr};
    }

    :host([appearance="lightweight"]) .content {
        position: relative;
    }

    :host([appearance="lightweight"]) .content::before {
        content: "";
        display: block;
        height: calc(${Et} * 1px);
        position: absolute;
        top: calc(1em + 4px);
        width: 100%;
    }

    :host([appearance="lightweight"]:hover) .content::before {
        background: ${Fr};
    }

    :host([appearance="lightweight"]:active) .content::before {
        background: ${Tr};
    }

    :host([appearance="lightweight"]) .control:${it.focusVisible} .content::before {
        background: ${on};
        height: calc(${qt} * 1px);
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
            :host([appearance="lightweight"]) .control:hover,
            :host([appearance="lightweight"]) .control:${it.focusVisible} {
                forced-color-adjust: none;
                background: ${za.ButtonFace};
                color: ${za.Highlight};
            }
            :host([appearance="lightweight"]) .control:hover .content::before,
            :host([appearance="lightweight"]) .control:${it.focusVisible} .content::before {
                background: ${za.Highlight};
            }

            :host([appearance="lightweight"][href]) .control:hover,
            :host([appearance="lightweight"][href]) .control:${it.focusVisible} {
                background: ${za.ButtonFace};
                box-shadow: none;
                color: ${za.LinkText};
            }

            :host([appearance="lightweight"][href]) .control:hover .content::before,
            :host([appearance="lightweight"][href]) .control:${it.focusVisible} .content::before {
                background: ${za.LinkText};
            }
        `));const Pa=oa.css`
    :host([appearance="outline"]) {
        background: transparent;
        border-color: ${ir};
    }

    :host([appearance="outline"]:hover) {
        border-color: ${lr};
    }

    :host([appearance="outline"]:active) {
        border-color: ${sr};
    }

    :host([appearance="outline"]) .control {
        border-color: inherit;
    }

    :host([appearance="outline"]) .control:${it.focusVisible} {
        box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px) ${Yr} inset;
        border-color: ${Yr};
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
            :host([appearance="outline"]) .control {
                border-color: ${za.ButtonText};
            }
            :host([appearance="outline"]) .control:${it.focusVisible} {
              forced-color-adjust: none;
              background-color: ${za.Highlight};
              border-color: ${za.ButtonText};
              box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px) ${za.ButtonText} inset;
              color: ${za.HighlightText};
              fill: currentColor;
            }
            :host([appearance="outline"][href]) .control {
                background: ${za.ButtonFace};
                border-color: ${za.LinkText};
                color: ${za.LinkText};
                fill: currentColor;
            }
            :host([appearance="outline"][href]) .control:hover,
            :host([appearance="outline"][href]) .control:${it.focusVisible} {
              forced-color-adjust: none;
              border-color: ${za.LinkText};
              box-shadow: 0 0 0 1px ${za.LinkText} inset;
            }
        `));const Ia=oa.css`
    :host([appearance="stealth"]) {
        background: ${Rr};
    }

    :host([appearance="stealth"]:hover) {
        background: ${Pr};
    }

    :host([appearance="stealth"]:active) {
        background: ${Ir};
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
            :host([appearance="stealth"]),
            :host([appearance="stealth"]) .control {
                forced-color-adjust: none;
                background: ${za.ButtonFace};
                border-color: transparent;
                color: ${za.ButtonText};
                fill: currentColor;
            }

            :host([appearance="stealth"]:hover) .control {
                background: ${za.Highlight};
                border-color: ${za.Highlight};
                color: ${za.HighlightText};
                fill: currentColor;
            }

            :host([appearance="stealth"]:${it.focusVisible}) .control {
                background: ${za.Highlight};
                box-shadow: 0 0 0 1px ${za.Highlight};
                color: ${za.HighlightText};
                fill: currentColor;
            }

            :host([appearance="stealth"][href]) .control {
                color: ${za.LinkText};
            }

            :host([appearance="stealth"][href]:hover) .control,
            :host([appearance="stealth"][href]:${it.focusVisible}) .control {
                background: ${za.LinkText};
                border-color: ${za.LinkText};
                color: ${za.HighlightText};
                fill: currentColor;
            }

            :host([appearance="stealth"][href]:${it.focusVisible}) .control {
                forced-color-adjust: none;
                box-shadow: 0 0 0 1px ${za.LinkText};
            }
        `));function Ma(e,t){return new it.PropertyStyleSheetBehavior("appearance",e,t)}const Ga=(e,t)=>oa.css`
        ${Ha}
    `.withBehaviors(Ma("accent",Na),Ma("hypertext",Aa),Ma("lightweight",Ra),Ma("outline",Pa),Ma("stealth",Ia));class _a extends it.Anchor{appearanceChanged(e,t){if(this.$fastController.isConnected){this.classList.remove(e);this.classList.add(t)}}connectedCallback(){super.connectedCallback();if(!this.appearance){this.appearance="neutral"}}defaultSlottedContentChanged(e,t){const o=this.defaultSlottedContent.filter((e=>e.nodeType===Node.ELEMENT_NODE));if(o.length===1&&o[0]instanceof SVGElement){this.control.classList.add("icon-only")}else{this.control.classList.remove("icon-only")}}}pa([oa.attr],_a.prototype,"appearance",void 0);const Ea=_a.compose({baseName:"anchor",baseClass:it.Anchor,template:it.anchorTemplate,styles:Ga,shadowOptions:{delegatesFocus:true}});const qa=_a.compose({baseName:"anchor",baseClass:it.Anchor,template:it.anchorTemplate,styles:Ga});const Wa=(e,t)=>oa.css`
    :host {
        contain: layout;
        display: block;
    }
`;const Ua=it.AnchoredRegion.compose({baseName:"anchored-region",template:it.anchoredRegionTemplate,styles:Wa});const Xa=(e,t)=>oa.css`
    ::slotted(${e.tagFor(it.Badge)}) {
        left: 0;
    }
`;const Za=(e,t)=>oa.css`
    ::slotted(${e.tagFor(it.Badge)}) {
        right: 0;
    }
`;const Ya=(e,t)=>oa.css`
        ${(0,it.display)("flex")} :host {
            position: relative;
            height: var(--avatar-size, var(--avatar-size-default));
            max-width: var(--avatar-size, var(--avatar-size-default));
            --avatar-size-default: calc(
                (
                        (${Nt} + ${It}) * ${Mt} +
                            ((${Mt} * 8) - 40)
                    ) * 1px
            );
            --avatar-text-size: ${Wt};
            --avatar-text-ratio: ${Mt};
        }

        .link {
            text-decoration: none;
            color: ${on};
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            min-width: 100%;
        }

        .square {
            border-radius: calc(${Pt} * 1px);
            min-width: 100%;
            overflow: hidden;
        }

        .circle {
            border-radius: 100%;
            min-width: 100%;
            overflow: hidden;
        }

        .backplate {
            position: relative;
            display: flex;
        }

        .media,
        ::slotted(img) {
            max-width: 100%;
            position: absolute;
            display: block;
        }

        .content {
            font-size: calc(
                (var(--avatar-text-size) + var(--avatar-size, var(--avatar-size-default))) /
                    var(--avatar-text-ratio)
            );
            line-height: var(--avatar-size, var(--avatar-size-default));
            display: block;
            min-height: var(--avatar-size, var(--avatar-size-default));
        }

        ::slotted(${e.tagFor(it.Badge)}) {
            position: absolute;
            display: block;
        }
    `.withBehaviors(new Sn(Za(e,t),Xa(e,t)));class Ja extends it.Avatar{}pa([(0,oa.attr)({attribute:"src"})],Ja.prototype,"imgSrc",void 0);pa([oa.attr],Ja.prototype,"alt",void 0);const Ka=oa.html`
    ${(0,oa.when)((e=>e.imgSrc),oa.html`
            <img
                src="${e=>e.imgSrc}"
                alt="${e=>e.alt}"
                slot="media"
                class="media"
                part="media"
            />
        `)}
`;const Qa=Ja.compose({baseName:"avatar",baseClass:it.Avatar,template:it.avatarTemplate,styles:Ya,media:Ka,shadowOptions:{delegatesFocus:true}});const ei=(e,t)=>oa.css`
  ::slotted(${e.tagFor(it.Badge)}) {
    left: 0;
  }
`;const ti=(e,t)=>oa.css`
  ::slotted(${e.tagFor(it.Badge)}) {
    right: 0;
  }
`;const oi=(e,t)=>oa.css`
    ${(0,it.display)("flex")} :host {
      position: relative;
      height: var(--avatar-size, var(--avatar-size-default));
      width: var(--avatar-size, var(--avatar-size-default));
      --avatar-size-default: calc(
        (
            (${Nt} + ${It}) * ${Mt} +
              ((${Mt} * 8) - 40)
          ) * 1px
      );
      --avatar-text-size: ${Wt};
      --avatar-text-ratio: ${Mt};
    }

    .link {
      text-decoration: none;
      color: ${on};
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      min-width: 100%;
    }

    .square {
      border-radius: calc(${Pt} * 1px);
      min-width: 100%;
      overflow: hidden;
    }

    .circle {
      border-radius: 100%;
      min-width: 100%;
      overflow: hidden;
    }

    .backplate {
      position: relative;
      display: flex;
      background-color: ${ir};
    }

    .media,
    ::slotted(img) {
      max-width: 100%;
      position: absolute;
      display: block;
    }

    .content {
      font-size: calc(
        (
            var(--avatar-text-size) +
              var(--avatar-size, var(--avatar-size-default))
          ) / var(--avatar-text-ratio)
      );
      color: ${ur};
      line-height: var(--avatar-size, var(--avatar-size-default));
      display: block;
      min-height: var(--avatar-size, var(--avatar-size-default));
    }

    ::slotted(${e.tagFor(it.Badge)}) {
      position: absolute;
      display: block;
    }
  `.withBehaviors(new Sn(ti(e,t),ei(e,t)));const ri=Ja.compose({baseName:"avatar",baseClass:it.Avatar,template:it.avatarTemplate,styles:oi,media:Ka,shadowOptions:{delegatesFocus:true}});const ni=(e,t)=>oa.css`
  ${(0,it.display)("inline-block")} :host {
    box-sizing: border-box;
    font-family: ${Ht};
    font-size: ${Xt};
    line-height: ${Zt};
  }

  .control {
    border-radius: calc(${Pt} * 1px);
    padding: calc(((${Mt} * 0.5) - ${Et}) * 1px)
      calc((${Mt} - ${Et}) * 1px);
    color: ${on};
    font-weight: 600;
    border: calc(${Et} * 1px) solid transparent;
    background-color: ${Dr};
  }

  .control[style] {
    font-weight: 400;
  }

  :host([circular]) .control {
    border-radius: 100px;
    padding: 0 calc(${Mt} * 1px);
    /* Need to work with Brian on width and height here */
    height: calc((${aa} - (${Mt} * 3)) * 1px);
    min-width: calc((${aa} - (${Mt} * 3)) * 1px);
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }
`;const ai=it.Badge.compose({baseName:"badge",template:it.badgeTemplate,styles:ni});const ii=(e,t)=>oa.css`
    ${(0,it.display)("inline-block")} :host {
        box-sizing: border-box;
        font-family: ${Ht};
        font-size: ${Wt};
        line-height: ${Ut};
    }

    .list {
        display: flex;
        flex-wrap: wrap;
    }
`;const li=it.Breadcrumb.compose({baseName:"breadcrumb",template:it.breadcrumbTemplate,styles:ii});const si=(e,t)=>oa.css`
    ${(0,it.display)("inline-flex")} :host {
        background: transparent;
        box-sizing: border-box;
        font-family: ${Ht};
        font-size: ${Wt};
        fill: currentColor;
        line-height: ${Ut};
        min-width: calc(${aa} * 1px);
        outline: none;
        color: ${on}
    }

    .listitem {
        display: flex;
        align-items: center;
        width: max-content;
    }

    .separator {
        margin: 0 6px;
        display: flex;
    }

    .control {
        align-items: center;
        box-sizing: border-box;
        color: ${kr};
        cursor: pointer;
        display: flex;
        fill: inherit;
        outline: none;
        text-decoration: none;
        white-space: nowrap;
    }

    .control:hover {
        color: ${Fr};
    }

    .control:active {
        color: ${Tr};
    }

    .control .content {
        position: relative;
    }

    .control .content::before {
        content: "";
        display: block;
        height: calc(${Et} * 1px);
        left: 0;
        position: absolute;
        right: 0;
        top: calc(1em + 4px);
        width: 100%;
    }

    .control:hover .content::before {
        background: ${Fr};
    }

    .control:active .content::before {
        background: ${Tr};
    }

    .control:${it.focusVisible} .content::before {
        background: ${Cr};
        height: calc(${qt} * 1px);
    }

    .control:not([href]) {
        color: ${on};
        cursor: default;
    }

    .control:not([href]) .content::before {
        background: none;
    }

    .start,
    .end {
        display: flex;
    }

    ::slotted(svg) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
    }

    .start {
        margin-inline-end: 6px;
    }

    .end {
        margin-inline-start: 6px;
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      .control:hover .content::before,
                .control:${it.focusVisible} .content::before {
        background: ${na.LinkText};
      }
      .start,
      .end {
        fill: ${na.ButtonText};
      }
    `));const ci=it.BreadcrumbItem.compose({baseName:"breadcrumb-item",template:it.breadcrumbItemTemplate,styles:si,separator:"/",shadowOptions:{delegatesFocus:true}});var di=function(e,t){di=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var o in t)if(Object.prototype.hasOwnProperty.call(t,o))e[o]=t[o]};return di(e,t)};function hi(e,t){if(typeof t!=="function"&&t!==null)throw new TypeError("Class extends value "+String(t)+" is not a constructor or null");di(e,t);function o(){this.constructor=e}e.prototype=t===null?Object.create(t):(o.prototype=t.prototype,new o)}var ui=function(){ui=Object.assign||function e(t){for(var o,r=1,n=arguments.length;r<n;r++){o=arguments[r];for(var a in o)if(Object.prototype.hasOwnProperty.call(o,a))t[a]=o[a]}return t};return ui.apply(this,arguments)};function pi(e,t){var o={};for(var r in e)if(Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0)o[r]=e[r];if(e!=null&&typeof Object.getOwnPropertySymbols==="function")for(var n=0,r=Object.getOwnPropertySymbols(e);n<r.length;n++){if(t.indexOf(r[n])<0&&Object.prototype.propertyIsEnumerable.call(e,r[n]))o[r[n]]=e[r[n]]}return o}function gi(e,t,o,r){var n=arguments.length,a=n<3?t:r===null?r=Object.getOwnPropertyDescriptor(t,o):r,i;if(typeof Reflect==="object"&&typeof Reflect.decorate==="function")a=Reflect.decorate(e,t,o,r);else for(var l=e.length-1;l>=0;l--)if(i=e[l])a=(n<3?i(a):n>3?i(t,o,a):i(t,o))||a;return n>3&&a&&Object.defineProperty(t,o,a),a}function bi(e,t){return function(o,r){t(o,r,e)}}function fi(e,t,o,r,n,a){function i(e){if(e!==void 0&&typeof e!=="function")throw new TypeError("Function expected");return e}var l=r.kind,s=l==="getter"?"get":l==="setter"?"set":"value";var c=!t&&e?r["static"]?e:e.prototype:null;var d=t||(c?Object.getOwnPropertyDescriptor(c,r.name):{});var h,u=false;for(var p=o.length-1;p>=0;p--){var g={};for(var b in r)g[b]=b==="access"?{}:r[b];for(var b in r.access)g.access[b]=r.access[b];g.addInitializer=function(e){if(u)throw new TypeError("Cannot add initializers after decoration has completed");a.push(i(e||null))};var f=(0,o[p])(l==="accessor"?{get:d.get,set:d.set}:d[s],g);if(l==="accessor"){if(f===void 0)continue;if(f===null||typeof f!=="object")throw new TypeError("Object expected");if(h=i(f.get))d.get=h;if(h=i(f.set))d.set=h;if(h=i(f.init))n.push(h)}else if(h=i(f)){if(l==="field")n.push(h);else d[s]=h}}if(c)Object.defineProperty(c,r.name,d);u=true}function $i(e,t,o){var r=arguments.length>2;for(var n=0;n<t.length;n++){o=r?t[n].call(e,o):t[n].call(e)}return r?o:void 0}function xi(e){return typeof e==="symbol"?e:"".concat(e)}function mi(e,t,o){if(typeof t==="symbol")t=t.description?"[".concat(t.description,"]"):"";return Object.defineProperty(e,"name",{configurable:true,value:o?"".concat(o," ",t):t})}function vi(e,t){if(typeof Reflect==="object"&&typeof Reflect.metadata==="function")return Reflect.metadata(e,t)}function yi(e,t,o,r){function n(e){return e instanceof o?e:new o((function(t){t(e)}))}return new(o||(o=Promise))((function(o,a){function i(e){try{s(r.next(e))}catch(t){a(t)}}function l(e){try{s(r["throw"](e))}catch(t){a(t)}}function s(e){e.done?o(e.value):n(e.value).then(i,l)}s((r=r.apply(e,t||[])).next())}))}function wi(e,t){var o={label:0,sent:function(){if(a[0]&1)throw a[1];return a[1]},trys:[],ops:[]},r,n,a,i;return i={next:l(0),throw:l(1),return:l(2)},typeof Symbol==="function"&&(i[Symbol.iterator]=function(){return this}),i;function l(e){return function(t){return s([e,t])}}function s(l){if(r)throw new TypeError("Generator is already executing.");while(i&&(i=0,l[0]&&(o=0)),o)try{if(r=1,n&&(a=l[0]&2?n["return"]:l[0]?n["throw"]||((a=n["return"])&&a.call(n),0):n.next)&&!(a=a.call(n,l[1])).done)return a;if(n=0,a)l=[l[0]&2,a.value];switch(l[0]){case 0:case 1:a=l;break;case 4:o.label++;return{value:l[1],done:false};case 5:o.label++;n=l[1];l=[0];continue;case 7:l=o.ops.pop();o.trys.pop();continue;default:if(!(a=o.trys,a=a.length>0&&a[a.length-1])&&(l[0]===6||l[0]===2)){o=0;continue}if(l[0]===3&&(!a||l[1]>a[0]&&l[1]<a[3])){o.label=l[1];break}if(l[0]===6&&o.label<a[1]){o.label=a[1];a=l;break}if(a&&o.label<a[2]){o.label=a[2];o.ops.push(l);break}if(a[2])o.ops.pop();o.trys.pop();continue}l=t.call(e,o)}catch(s){l=[6,s];n=0}finally{r=a=0}if(l[0]&5)throw l[1];return{value:l[0]?l[1]:void 0,done:true}}}var ki=Object.create?function(e,t,o,r){if(r===undefined)r=o;var n=Object.getOwnPropertyDescriptor(t,o);if(!n||("get"in n?!t.__esModule:n.writable||n.configurable)){n={enumerable:true,get:function(){return t[o]}}}Object.defineProperty(e,r,n)}:function(e,t,o,r){if(r===undefined)r=o;e[r]=t[o]};function Fi(e,t){for(var o in e)if(o!=="default"&&!Object.prototype.hasOwnProperty.call(t,o))ki(t,e,o)}function Ti(e){var t=typeof Symbol==="function"&&Symbol.iterator,o=t&&e[t],r=0;if(o)return o.call(e);if(e&&typeof e.length==="number")return{next:function(){if(e&&r>=e.length)e=void 0;return{value:e&&e[r++],done:!e}}};throw new TypeError(t?"Object is not iterable.":"Symbol.iterator is not defined.")}function Ci(e,t){var o=typeof Symbol==="function"&&e[Symbol.iterator];if(!o)return e;var r=o.call(e),n,a=[],i;try{while((t===void 0||t-- >0)&&!(n=r.next()).done)a.push(n.value)}catch(l){i={error:l}}finally{try{if(n&&!n.done&&(o=r["return"]))o.call(r)}finally{if(i)throw i.error}}return a}function Vi(){for(var e=[],t=0;t<arguments.length;t++)e=e.concat(Ci(arguments[t]));return e}function Di(){for(var e=0,t=0,o=arguments.length;t<o;t++)e+=arguments[t].length;for(var r=Array(e),n=0,t=0;t<o;t++)for(var a=arguments[t],i=0,l=a.length;i<l;i++,n++)r[n]=a[i];return r}function Si(e,t,o){if(o||arguments.length===2)for(var r=0,n=t.length,a;r<n;r++){if(a||!(r in t)){if(!a)a=Array.prototype.slice.call(t,0,r);a[r]=t[r]}}return e.concat(a||Array.prototype.slice.call(t))}function ji(e){return this instanceof ji?(this.v=e,this):new ji(e)}function Bi(e,t,o){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var r=o.apply(e,t||[]),n,a=[];return n={},i("next"),i("throw"),i("return"),n[Symbol.asyncIterator]=function(){return this},n;function i(e){if(r[e])n[e]=function(t){return new Promise((function(o,r){a.push([e,t,o,r])>1||l(e,t)}))}}function l(e,t){try{s(r[e](t))}catch(o){h(a[0][3],o)}}function s(e){e.value instanceof ji?Promise.resolve(e.value.v).then(c,d):h(a[0][2],e)}function c(e){l("next",e)}function d(e){l("throw",e)}function h(e,t){if(e(t),a.shift(),a.length)l(a[0][0],a[0][1])}}function Oi(e){var t,o;return t={},r("next"),r("throw",(function(e){throw e})),r("return"),t[Symbol.iterator]=function(){return this},t;function r(r,n){t[r]=e[r]?function(t){return(o=!o)?{value:ji(e[r](t)),done:false}:n?n(t):t}:n}}function zi(e){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var t=e[Symbol.asyncIterator],o;return t?t.call(e):(e=typeof Ti==="function"?Ti(e):e[Symbol.iterator](),o={},r("next"),r("throw"),r("return"),o[Symbol.asyncIterator]=function(){return this},o);function r(t){o[t]=e[t]&&function(o){return new Promise((function(r,a){o=e[t](o),n(r,a,o.done,o.value)}))}}function n(e,t,o,r){Promise.resolve(r).then((function(t){e({value:t,done:o})}),t)}}function Li(e,t){if(Object.defineProperty){Object.defineProperty(e,"raw",{value:t})}else{e.raw=t}return e}var Hi=Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:true,value:t})}:function(e,t){e["default"]=t};function Ni(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var o in e)if(o!=="default"&&Object.prototype.hasOwnProperty.call(e,o))ki(t,e,o);Hi(t,e);return t}function Ai(e){return e&&e.__esModule?e:{default:e}}function Ri(e,t,o,r){if(o==="a"&&!r)throw new TypeError("Private accessor was defined without a getter");if(typeof t==="function"?e!==t||!r:!t.has(e))throw new TypeError("Cannot read private member from an object whose class did not declare it");return o==="m"?r:o==="a"?r.call(e):r?r.value:t.get(e)}function Pi(e,t,o,r,n){if(r==="m")throw new TypeError("Private method is not writable");if(r==="a"&&!n)throw new TypeError("Private accessor was defined without a setter");if(typeof t==="function"?e!==t||!n:!t.has(e))throw new TypeError("Cannot write private member to an object whose class did not declare it");return r==="a"?n.call(e,o):n?n.value=o:t.set(e,o),o}function Ii(e,t){if(t===null||typeof t!=="object"&&typeof t!=="function")throw new TypeError("Cannot use 'in' operator on non-object");return typeof e==="function"?t===e:e.has(t)}function Mi(e,t){return new it.PropertyStyleSheetBehavior("appearance",e,t)}const Gi=oa.css`
  ${(0,it.display)("inline-flex")} :host {
    font-family: ${Ht};
    outline: none;
    font-size: ${Wt};
    line-height: ${Ut};
    height: calc(${aa} * 1px);
    min-width: calc(${aa} * 1px);
    background-color: ${Dr};
    color: ${on};
    border-radius: calc(${Pt} * 1px);
    fill: currentcolor;
    cursor: pointer;
    margin: calc((${qt} + 2) * 1px);
  }

  .control {
    background: transparent;
    height: inherit;
    flex-grow: 1;
    box-sizing: border-box;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    padding: 0 calc((10 + (${Mt} * 2 * ${It})) * 1px);
    white-space: nowrap;
    outline: none;
    text-decoration: none;
    border: calc(${Et} * 1px) solid transparent;
    color: inherit;
    border-radius: inherit;
    fill: inherit;
    cursor: inherit;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
  }

  :host(:hover) {
    background-color: ${Sr};
  }

  :host(:active) {
    background-color: ${jr};
  }

  :host([aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${qr};
  }

  :host([minimal]) {
    --density: -4;
  }

  :host([minimal]) .control {
    padding: 1px;
  }

  /* prettier-ignore */
  .control:${it.focusVisible} {
    outline: calc(${qt} * 1px) solid ${Wr};
    outline-offset: 2px;
    -moz-outline-radius: 0px;
  }

  .control::-moz-focus-inner {
    border: 0;
  }

  .start,
  .end {
    display: flex;
  }

  .control.icon-only {
    padding: 0;
    line-height: 0;
  }

  ::slotted(svg) {
    ${""} width: 16px;
    height: 16px;
    pointer-events: none;
  }

  .start {
    margin-inline-end: 11px;
  }

  .end {
    margin-inline-start: 11px;
  }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
    :host .control {
      background-color: ${na.ButtonFace};
      border-color: ${na.ButtonText};
      color: ${na.ButtonText};
      fill: currentColor;
    }

    :host(:hover) .control {
      forced-color-adjust: none;
      background-color: ${na.Highlight};
      color: ${na.HighlightText};
    }

    /* prettier-ignore */
    .control:${it.focusVisible} {
        forced-color-adjust: none;
        background-color: ${na.Highlight};
        outline-color: ${na.ButtonText};
        color: ${na.HighlightText};
      }

    .control:hover,
    :host([appearance='outline']) .control:hover {
      border-color: ${na.ButtonText};
    }

    :host([href]) .control {
      border-color: ${na.LinkText};
      color: ${na.LinkText};
    }

    :host([href]) .control:hover,
      :host([href]) .control:${it.focusVisible} {
      forced-color-adjust: none;
      background: ${na.ButtonFace};
      outline-color: ${na.LinkText};
      color: ${na.LinkText};
      fill: currentColor;
    }
  `));const _i=oa.css`
  :host([appearance='accent']) {
    background: ${ir};
    color: ${ur};
  }

  :host([appearance='accent']:hover) {
    background: ${lr};
    color: ${pr};
  }

  :host([appearance='accent'][aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${Tr};
  }

  :host([appearance='accent']:active) .control:active {
    background: ${sr};
    color: ${gr};
  }

  :host([appearance="accent"]) .control:${it.focusVisible} {
    outline-color: ${cr};
  }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
    :host([appearance='accent']) .control {
      forced-color-adjust: none;
      background: ${na.Highlight};
      color: ${na.HighlightText};
    }

    :host([appearance='accent']) .control:hover,
    :host([appearance='accent']:active) .control:active {
      background: ${na.HighlightText};
      border-color: ${na.Highlight};
      color: ${na.Highlight};
    }

    :host([appearance="accent"]) .control:${it.focusVisible} {
      outline-color: ${na.Highlight};
    }

    :host([appearance='accent'][href]) .control {
      background: ${na.LinkText};
      color: ${na.HighlightText};
    }

    :host([appearance='accent'][href]) .control:hover {
      background: ${na.ButtonFace};
      border-color: ${na.LinkText};
      box-shadow: none;
      color: ${na.LinkText};
      fill: currentColor;
    }

    :host([appearance="accent"][href]) .control:${it.focusVisible} {
      outline-color: ${na.HighlightText};
    }
  `));const Ei=oa.css`
  :host([appearance='error']) {
    background: ${Ln};
    color: ${ur};
  }

  :host([appearance='error']:hover) {
    background: ${Hn};
    color: ${pr};
  }

  :host([appearance='error'][aria-pressed='true']) {
    box-shadow: inset 0px 0px 2px 2px ${Qn};
  }

  :host([appearance='error']:active) .control:active {
    background: ${Nn};
    color: ${gr};
  }

  :host([appearance="error"]) .control:${it.focusVisible} {
    outline-color: ${An};
  }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
    :host([appearance='error']) .control {
      forced-color-adjust: none;
      background: ${na.Highlight};
      color: ${na.HighlightText};
    }

    :host([appearance='error']) .control:hover,
    :host([appearance='error']:active) .control:active {
      background: ${na.HighlightText};
      border-color: ${na.Highlight};
      color: ${na.Highlight};
    }

    :host([appearance="error"]) .control:${it.focusVisible} {
      outline-color: ${na.Highlight};
    }

    :host([appearance='error'][href]) .control {
      background: ${na.LinkText};
      color: ${na.HighlightText};
    }

    :host([appearance='error'][href]) .control:hover {
      background: ${na.ButtonFace};
      border-color: ${na.LinkText};
      box-shadow: none;
      color: ${na.LinkText};
      fill: currentColor;
    }

    :host([appearance="error"][href]) .control:${it.focusVisible} {
      outline-color: ${na.HighlightText};
    }
  `));const qi=oa.css`
  :host([appearance='lightweight']) {
    background: transparent;
    color: ${kr};
  }

  :host([appearance='lightweight']) .control {
    padding: 0;
    height: initial;
    border: none;
    box-shadow: none;
    border-radius: 0;
  }

  :host([appearance='lightweight']:hover) {
    background: transparent;
    color: ${Fr};
  }

  :host([appearance='lightweight']:active) {
    background: transparent;
    color: ${Tr};
  }

  :host([appearance='lightweight']) .content {
    position: relative;
  }

  :host([appearance='lightweight']) .content::before {
    content: '';
    display: block;
    height: calc(${Et} * 1px);
    position: absolute;
    top: calc(1em + 4px);
    width: 100%;
  }

  :host([appearance='lightweight']:hover) .content::before {
    background: ${Fr};
  }

  :host([appearance='lightweight']:active) .content::before {
    background: ${Tr};
  }

  :host([appearance="lightweight"]) .control:${it.focusVisible} {
    outline-color: transparent;
  }

  :host([appearance="lightweight"]) .control:${it.focusVisible} .content::before {
    background: ${on};
    height: calc(${qt} * 1px);
  }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
    :host([appearance="lightweight"]) .control:hover,
      :host([appearance="lightweight"]) .control:${it.focusVisible} {
      forced-color-adjust: none;
      background: ${na.ButtonFace};
      color: ${na.Highlight};
    }
    :host([appearance="lightweight"]) .control:hover .content::before,
      :host([appearance="lightweight"]) .control:${it.focusVisible} .content::before {
      background: ${na.Highlight};
    }

    :host([appearance="lightweight"][href]) .control:hover,
      :host([appearance="lightweight"][href]) .control:${it.focusVisible} {
      background: ${na.ButtonFace};
      box-shadow: none;
      color: ${na.LinkText};
    }

    :host([appearance="lightweight"][href]) .control:hover .content::before,
      :host([appearance="lightweight"][href]) .control:${it.focusVisible} .content::before {
      background: ${na.LinkText};
    }
  `));const Wi=oa.css`
  :host([appearance='outline']) {
    background: transparent;
    border-color: ${ir};
  }

  :host([appearance='outline']:hover) {
    border-color: ${lr};
  }

  :host([appearance='outline']:active) {
    border-color: ${sr};
  }

  :host([appearance='outline']) .control {
    border-color: inherit;
  }

  :host([appearance="outline"]) .control:${it.focusVisible} {
    outline-color: ${cr};
  }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
    :host([appearance='outline']) .control {
      border-color: ${na.ButtonText};
    }
    :host([appearance="outline"]) .control:${it.focusVisible} {
      forced-color-adjust: none;
      background-color: ${na.Highlight};
      outline-color: ${na.ButtonText};
      color: ${na.HighlightText};
      fill: currentColor;
    }
    :host([appearance='outline'][href]) .control {
      background: ${na.ButtonFace};
      border-color: ${na.LinkText};
      color: ${na.LinkText};
      fill: currentColor;
    }
    :host([appearance="outline"][href]) .control:hover,
      :host([appearance="outline"][href]) .control:${it.focusVisible} {
      forced-color-adjust: none;
      outline-color: ${na.LinkText};
    }
  `));const Ui=oa.css`
  :host([appearance='stealth']) {
    background: transparent;
  }

  :host([appearance='stealth']:hover) {
    background: ${Pr};
  }

  :host([appearance='stealth']:active) {
    background: ${Ir};
  }

  :host([appearance='stealth']) .control:${it.focusVisible} {
    outline-color: ${cr};
  }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
    :host([appearance='stealth']),
    :host([appearance='stealth']) .control {
      forced-color-adjust: none;
      background: ${na.ButtonFace};
      border-color: transparent;
      color: ${na.ButtonText};
      fill: currentColor;
    }

    :host([appearance='stealth']:hover) .control {
      background: ${na.Highlight};
      border-color: ${na.Highlight};
      color: ${na.HighlightText};
      fill: currentColor;
    }

    :host([appearance="stealth"]:${it.focusVisible}) .control {
      outline-color: ${na.Highlight};
      color: ${na.HighlightText};
      fill: currentColor;
    }

    :host([appearance='stealth'][href]) .control {
      color: ${na.LinkText};
    }

    :host([appearance="stealth"][href]:hover) .control,
      :host([appearance="stealth"][href]:${it.focusVisible}) .control {
      background: ${na.LinkText};
      border-color: ${na.LinkText};
      color: ${na.HighlightText};
      fill: currentColor;
    }

    :host([appearance="stealth"][href]:${it.focusVisible}) .control {
      forced-color-adjust: none;
      box-shadow: 0 0 0 1px ${na.LinkText};
    }
  `));const Xi=(e,t)=>oa.css`
    :host([disabled]),
    :host([disabled]:hover),
    :host([disabled]:active) {
      opacity: ${_t};
      background-color: ${Dr};
      cursor: ${it.disabledCursor};
    }

    ${Gi}
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host([disabled]),
      :host([disabled]) .control,
      :host([disabled]:hover),
      :host([disabled]:active) {
        forced-color-adjust: none;
        background-color: ${na.ButtonFace};
        outline-color: ${na.GrayText};
        color: ${na.GrayText};
        cursor: ${it.disabledCursor};
        opacity: 1;
      }
    `),Mi("accent",oa.css`
        :host([appearance='accent'][disabled]),
        :host([appearance='accent'][disabled]:hover),
        :host([appearance='accent'][disabled]:active) {
          background: ${ir};
        }

        ${_i}
      `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
          :host([appearance='accent'][disabled]) .control,
          :host([appearance='accent'][disabled]) .control:hover {
            background: ${na.ButtonFace};
            border-color: ${na.GrayText};
            color: ${na.GrayText};
          }
        `))),Mi("error",oa.css`
        :host([appearance='error'][disabled]),
        :host([appearance='error'][disabled]:hover),
        :host([appearance='error'][disabled]:active) {
          background: ${Ln};
        }

        ${Ei}
      `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
          :host([appearance='error'][disabled]) .control,
          :host([appearance='error'][disabled]) .control:hover {
            background: ${na.ButtonFace};
            border-color: ${na.GrayText};
            color: ${na.GrayText};
          }
        `))),Mi("lightweight",oa.css`
        :host([appearance='lightweight'][disabled]:hover),
        :host([appearance='lightweight'][disabled]:active) {
          background-color: transparent;
          color: ${kr};
        }

        :host([appearance='lightweight'][disabled]) .content::before,
        :host([appearance='lightweight'][disabled]:hover) .content::before,
        :host([appearance='lightweight'][disabled]:active) .content::before {
          background: transparent;
        }

        ${qi}
      `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
          :host([appearance='lightweight'].disabled) .control {
            forced-color-adjust: none;
            color: ${na.GrayText};
          }

          :host([appearance='lightweight'].disabled)
            .control:hover
            .content::before {
            background: none;
          }
        `))),Mi("outline",oa.css`
        :host([appearance='outline'][disabled]),
        :host([appearance='outline'][disabled]:hover),
        :host([appearance='outline'][disabled]:active) {
          background: transparent;
          border-color: ${ir};
        }

        ${Wi}
      `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
          :host([appearance='outline'][disabled]) .control {
            border-color: ${na.GrayText};
          }
        `))),Mi("stealth",oa.css`
        :host([appearance='stealth'][disabled]),
        :host([appearance='stealth'][disabled]:hover),
        :host([appearance='stealth'][disabled]:active) {
          background: ${Rr};
        }

        ${Ui}
      `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
          :host([appearance='stealth'][disabled]) {
            background: ${na.ButtonFace};
          }

          :host([appearance='stealth'][disabled]) .control {
            background: ${na.ButtonFace};
            border-color: transparent;
            color: ${na.GrayText};
          }
        `))));class Zi extends it.Button{connectedCallback(){super.connectedCallback();if(!this.appearance){this.appearance="neutral"}}defaultSlottedContentChanged(e,t){const o=this.defaultSlottedContent.filter((e=>e.nodeType===Node.ELEMENT_NODE));if(o.length===1&&(o[0]instanceof SVGElement||o[0].classList.contains("fa")||o[0].classList.contains("fas"))){this.control.classList.add("icon-only")}else{this.control.classList.remove("icon-only")}}}gi([oa.attr],Zi.prototype,"appearance",void 0);gi([(0,oa.attr)({attribute:"minimal",mode:"boolean"})],Zi.prototype,"minimal",void 0);const Yi=Zi.compose({baseName:"button",baseClass:it.Button,template:it.buttonTemplate,styles:Xi,shadowOptions:{delegatesFocus:true}});const Ji="0 0 calc((var(--elevation) * 0.225px) + 2px) rgba(0, 0, 0, calc(.11 * (2 - var(--background-luminance, 1))))";const Ki="0 calc(var(--elevation) * 0.4px) calc((var(--elevation) * 0.9px)) rgba(0, 0, 0, calc(.13 * (2 - var(--background-luminance, 1))))";const Qi=`box-shadow: ${Ji}, ${Ki};`;const el=(e,t)=>oa.css`
        ${(0,it.display)("block")} :host {
            --elevation: 4;
            display: block;
            contain: content;
            height: var(--card-height, 100%);
            width: var(--card-width, 100%);
            box-sizing: border-box;
            background: ${rr};
            border-radius: calc(${Pt} * 1px);
            ${Qi}
        }
    `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                :host {
                    forced-color-adjust: none;
                    background: ${za.Canvas};
                    box-shadow: 0 0 0 1px ${za.CanvasText};
                }
            `));class tl extends it.Card{connectedCallback(){super.connectedCallback();const e=(0,it.composedParent)(this);if(e){rr.setValueFor(this,(t=>Ur.getValueFor(t).evaluate(t,rr.getValueFor(e))))}}}const ol=tl.compose({baseName:"card",baseClass:it.Card,template:it.cardTemplate,styles:el});const rl=tl.compose({baseName:"card",baseClass:it.Card,template:it.cardTemplate,styles:el});const nl=(e,t)=>oa.css`
    ${(0,it.display)("inline-flex")} :host {
      align-items: center;
      outline: none;
      margin: calc(${Mt} * 1px) 0;
      /* Chromium likes to select label text or the default slot when the checkbox is
            clicked. Maybe there is a better solution here? */
      user-select: none;
    }

    .control {
      position: relative;
      width: calc((${aa} / 2 + ${Mt}) * 1px);
      height: calc((${aa} / 2 + ${Mt}) * 1px);
      box-sizing: border-box;
      border-radius: calc(${Pt} * 1px);
      border: calc(${Et} * 1px) solid ${nn};
      background: ${zr};
      outline: none;
      cursor: pointer;
    }

    .label {
      font-family: ${Ht};
      color: ${on};
      /* Need to discuss with Brian how HorizontalSpacingNumber can work.
            https://github.com/microsoft/fast/issues/2766 */
      padding-inline-start: calc(${Mt} * 2px + 2px);
      margin-inline-end: calc(${Mt} * 2px + 2px);
      cursor: pointer;
      font-size: ${Wt};
      line-height: ${Ut};
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    .checked-indicator {
      width: 100%;
      height: 100%;
      display: block;
      fill: ${ur};
      opacity: 0;
      pointer-events: none;
    }

    .indeterminate-indicator {
      border-radius: calc(${Pt} * 1px);
      background: ${ur};
      position: absolute;
      top: 50%;
      left: 50%;
      width: 50%;
      height: 50%;
      transform: translate(-50%, -50%);
      opacity: 0;
    }

    :host(:not([disabled])) .control:hover {
      background: ${Lr};
      border-color: ${an};
    }

    :host(:not([disabled])) .control:active {
      background: ${Hr};
      border-color: ${ln};
    }

    :host(:${it.focusVisible}) .control {
      outline: calc(${qt} * 1px) solid ${cr};
      outline-offset: 2px;
    }

    :host([aria-checked='true']) .control {
      background: ${ir};
      border: calc(${Et} * 1px) solid ${ir};
    }

    :host([aria-checked='true']:not([disabled])) .control:hover {
      background: ${lr};
      border: calc(${Et} * 1px) solid ${lr};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .checked-indicator {
      fill: ${pr};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .indeterminate-indicator {
      background: ${pr};
    }

    :host([aria-checked='true']:not([disabled])) .control:active {
      background: ${sr};
      border: calc(${Et} * 1px) solid ${sr};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .checked-indicator {
      fill: ${gr};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .indeterminate-indicator {
      background: ${gr};
    }

    :host([aria-checked="true"]:${it.focusVisible}:not([disabled])) .control {
      outline: calc(${qt} * 1px) solid ${cr};
      outline-offset: 2px;
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${it.disabledCursor};
    }

    :host([aria-checked='true']:not(.indeterminate)) .checked-indicator,
    :host(.indeterminate) .indeterminate-indicator {
      opacity: 1;
    }

    :host([disabled]) {
      opacity: ${_t};
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      .control {
        forced-color-adjust: none;
        border-color: ${na.FieldText};
        background: ${na.Field};
      }
      .checked-indicator {
        fill: ${na.FieldText};
      }
      .indeterminate-indicator {
        background: ${na.FieldText};
      }
      :host(:not([disabled])) .control:hover,
      .control:active {
        border-color: ${na.Highlight};
        background: ${na.Field};
      }
      :host(:${it.focusVisible}) .control {
        outline: calc(${qt} * 1px) solid ${na.FieldText};
        outline-offset: 2px;
      }
      :host([aria-checked="true"]:${it.focusVisible}:not([disabled])) .control {
        outline: calc(${qt} * 1px) solid ${na.FieldText};
        outline-offset: 2px;
      }
      :host([aria-checked='true']) .control {
        background: ${na.Highlight};
        border-color: ${na.Highlight};
      }
      :host([aria-checked='true']:not([disabled])) .control:hover,
      .control:active {
        border-color: ${na.Highlight};
        background: ${na.HighlightText};
      }
      :host([aria-checked='true']) .checked-indicator {
        fill: ${na.HighlightText};
      }
      :host([aria-checked='true']:not([disabled]))
        .control:hover
        .checked-indicator {
        fill: ${na.Highlight};
      }
      :host([aria-checked='true']) .indeterminate-indicator {
        background: ${na.HighlightText};
      }
      :host([aria-checked='true']) .control:hover .indeterminate-indicator {
        background: ${na.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host([disabled]) .control {
        forced-color-adjust: none;
        border-color: ${na.GrayText};
        background: ${na.Field};
      }
      :host([disabled]) .indeterminate-indicator,
      :host([aria-checked='true'][disabled])
        .control:hover
        .indeterminate-indicator {
        forced-color-adjust: none;
        background: ${na.GrayText};
      }
      :host([disabled]) .checked-indicator,
      :host([aria-checked='true'][disabled]) .control:hover .checked-indicator {
        forced-color-adjust: none;
        fill: ${na.GrayText};
      }
    `));const al=it.Checkbox.compose({baseName:"checkbox",template:it.checkboxTemplate,styles:nl,checkedIndicator:`\n    <svg\n      part="checked-indicator"\n      class="checked-indicator"\n      viewBox="0 0 20 20"\n      xmlns="http://www.w3.org/2000/svg"\n    >\n      <path\n        fill-rule="evenodd"\n        clip-rule="evenodd"\n        d="M8.143 12.6697L15.235 4.5L16.8 5.90363L8.23812 15.7667L3.80005 11.2556L5.27591 9.7555L8.143 12.6697Z"\n      />\n    </svg>\n    `,indeterminateIndicator:`\n        <div part="indeterminate-indicator" class="indeterminate-indicator"></div>\n    `});const il="0 0 calc((var(--elevation) * 0.225px) + 2px) rgba(0, 0, 0, calc(.11 * (2 - var(--background-luminance, 1))))";const ll="0 calc(var(--elevation) * 0.4px) calc((var(--elevation) * 0.9px)) rgba(0, 0, 0, calc(.13 * (2 - var(--background-luminance, 1))))";const sl=`box-shadow: ${il}, ${ll};`;const cl=(e,t)=>oa.css`
    ${(0,it.display)("inline-flex")} :host {
      --elevation: 14;
      background: ${zr};
      border-radius: calc(${Pt} * 1px);
      border: calc(${Et} * 1px) solid ${_r};
      box-sizing: border-box;
      color: ${on};
      font-family: ${Ht};
      height: calc(${aa} * 1px);
      position: relative;
      user-select: none;
      outline: none;
      vertical-align: top;
    }

    :host(:not([autowidth])) {
      min-width: 250px;
    }

    .listbox {
      ${sl}
      background: ${Xo};
      border: calc(${Et} * 1px) solid ${nn};
      border-radius: calc(${Pt} * 1px);
      box-sizing: border-box;
      display: inline-flex;
      flex-direction: column;
      left: 0;
      max-height: calc(var(--max-height) - (${aa} * 1px));
      padding: calc(${Mt} * 1px) 0;
      overflow-y: auto;
      position: absolute;
      z-index: 1;
    }

    :host(:not([autowidth])) .listbox {
      width: 100%;
    }

    :host([autowidth]) ::slotted([role='option']),
    :host([autowidth]) ::slotted(option) {
      padding: 0 calc(1em + ${Mt} * 1.25px + 1px);
    }

    .listbox[hidden] {
      display: none;
    }

    .control {
      align-items: center;
      box-sizing: border-box;
      cursor: pointer;
      display: flex;
      font-size: ${Wt};
      font-family: inherit;
      line-height: ${Ut};
      min-height: 100%;
      padding: 0 calc(${Mt} * 2.25px);
      width: 100%;
    }

    :host([minimal]) {
      --density: -4;
    }

    :host(:not([disabled]):hover) {
      background: ${Lr};
      border-color: ${Er};
    }

    :host(:${it.focusVisible}) {
      border-color: ${cr};
      box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px)
        ${cr};
    }

    :host([disabled]) {
      cursor: ${it.disabledCursor};
      opacity: ${_t};
    }

    :host([disabled]) .control {
      cursor: ${it.disabledCursor};
      user-select: none;
    }

    :host([disabled]:hover) {
      background: ${Rr};
      color: ${on};
      fill: currentcolor;
    }

    :host(:not([disabled])) .control:active {
      background: ${Hr};
      border-color: ${sr};
      border-radius: calc(${Pt} * 1px);
    }

    :host([open][position='above']) .listbox {
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
    }

    :host([open][position='below']) .listbox {
      border-top-left-radius: 0;
      border-top-right-radius: 0;
    }

    :host([open][position='above']) .listbox {
      border-bottom: 0;
      bottom: calc(${aa} * 1px);
    }

    :host([open][position='below']) .listbox {
      border-top: 0;
      top: calc(${aa} * 1px);
    }

    .selected-value {
      flex: 1 1 auto;
      font-family: inherit;
      text-align: start;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }

    .indicator {
      flex: 0 0 auto;
      margin-inline-start: 1em;
    }

    slot[name='listbox'] {
      display: none;
      width: 100%;
    }

    :host([open]) slot[name='listbox'] {
      display: flex;
      position: absolute;
      ${sl}
    }

    .end {
      margin-inline-start: auto;
    }

    .start,
    .end,
    .indicator,
    .select-indicator,
    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      fill: currentcolor;
      height: 1em;
      min-height: calc(${Mt} * 4px);
      min-width: calc(${Mt} * 4px);
      width: 1em;
    }

    ::slotted([role='option']),
    ::slotted(option) {
      flex: 0 0 auto;
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host(:not([disabled]):hover),
      :host(:not([disabled]):active) {
        border-color: ${na.Highlight};
      }

      :host(:not([disabled]):${it.focusVisible}) {
        background-color: ${na.ButtonFace};
        box-shadow: 0 0 0 calc(${qt} * 1px)
          ${na.Highlight};
        color: ${na.ButtonText};
        fill: currentcolor;
        forced-color-adjust: none;
      }

      :host(:not([disabled]):${it.focusVisible}) .listbox {
        background: ${na.ButtonFace};
      }

      :host([disabled]) {
        border-color: ${na.GrayText};
        background-color: ${na.ButtonFace};
        color: ${na.GrayText};
        fill: currentcolor;
        opacity: 1;
        forced-color-adjust: none;
      }

      :host([disabled]:hover) {
        background: ${na.ButtonFace};
      }

      :host([disabled]) .control {
        color: ${na.GrayText};
        border-color: ${na.GrayText};
      }

      :host([disabled]) .control .select-indicator {
        fill: ${na.GrayText};
      }

      :host(:${it.focusVisible}) ::slotted([aria-selected="true"][role="option"]),
            :host(:${it.focusVisible}) ::slotted(option[aria-selected="true"]),
            :host(:${it.focusVisible}) ::slotted([aria-selected="true"][role="option"]:not([disabled])) {
        background: ${na.Highlight};
        border-color: ${na.ButtonText};
        box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px)
          ${na.HighlightText};
        color: ${na.HighlightText};
        fill: currentcolor;
      }

      .start,
      .end,
      .indicator,
      .select-indicator,
      ::slotted(svg) {
        color: ${na.ButtonText};
        fill: currentcolor;
      }
    `));const dl=(e,t)=>oa.css`
  ${cl(e,t)}

  :host(:empty) .listbox {
    display: none;
  }

  :host([disabled]) *,
  :host([disabled]) {
    cursor: ${it.disabledCursor};
    user-select: none;
  }

  :host(:focus-within:not([disabled])) {
    border-color: ${cr};
    box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px)
      ${cr};
  }

  .selected-value {
    -webkit-appearance: none;
    background: transparent;
    border: none;
    color: inherit;
    font-size: ${Wt};
    line-height: ${Ut};
    height: calc(100% - (${Et} * 1px));
    margin: auto 0;
    width: 100%;
  }

  .selected-value:hover,
  .selected-value:${it.focusVisible},
  .selected-value:disabled,
  .selected-value:active {
    outline: none;
  }
`;class hl extends it.Combobox{connectedCallback(){super.connectedCallback();this.setAutoWidth()}slottedOptionsChanged(e,t){super.slottedOptionsChanged(e,t);this.setAutoWidth()}autoWidthChanged(e,t){if(t){this.setAutoWidth()}else{this.style.removeProperty("width")}}setAutoWidth(){if(!this.autoWidth||!this.isConnected){return}let e=this.listbox.getBoundingClientRect().width;if(e===0&&this.listbox.hidden){Object.assign(this.listbox.style,{visibility:"hidden"});this.listbox.removeAttribute("hidden");e=this.listbox.getBoundingClientRect().width;this.listbox.setAttribute("hidden","");this.listbox.style.removeProperty("visibility")}if(e>0){Object.assign(this.style,{width:`${e}px`})}}}gi([(0,oa.attr)({attribute:"autowidth",mode:"boolean"})],hl.prototype,"autoWidth",void 0);gi([(0,oa.attr)({attribute:"minimal",mode:"boolean"})],hl.prototype,"minimal",void 0);const ul=hl.compose({baseName:"combobox",baseClass:it.Combobox,template:it.comboboxTemplate,styles:dl,shadowOptions:{delegatesFocus:true},indicator:`\n    <svg\n      class="select-indicator"\n      part="select-indicator"\n      viewBox="0 0 12 7"\n      xmlns="http://www.w3.org/2000/svg"\n    >\n      <path\n        d="M11.85.65c.2.2.2.5 0 .7L6.4 6.84a.55.55 0 01-.78 0L.14 1.35a.5.5 0 11.71-.7L6 5.8 11.15.65c.2-.2.5-.2.7 0z"\n      />\n    </svg>\n    `});const pl=(e,t)=>oa.css`
    :host {
        display: grid;
        padding: 1px 0;
        box-sizing: border-box;
        width: 100%;
        border-bottom: calc(${Et} * 1px) solid ${dn};
    }

    :host(.header) {
    }

    :host(.sticky-header) {
        background: ${Dr};
        position: sticky;
        top: 0;
    }
`;const gl=(e,t)=>oa.css`
    :host {
        display: flex;
        position: relative;
        flex-direction: column;
    }
`;const bl=(e,t)=>oa.css`
    :host {
      padding: calc(${Mt} * 1px) calc(${Mt} * 3px);
      color: ${on};
      box-sizing: border-box;
      font-family: ${Ht};
      font-size: ${Wt};
      line-height: ${Ut};
      border: transparent calc(${Et} * 1px) solid;
      font-weight: 400;
      overflow: hidden;
      white-space: nowrap;
      border-radius: calc(${Pt} * 1px);
    }

    :host(.column-header) {
      font-weight: 600;
    }

    :host(:${it.focusVisible}) {
      outline: calc(${qt} * 1px) solid ${cr};
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        background: ${na.Field};
        color: ${na.FieldText};
      }

      :host(:${it.focusVisible}) {
        border-color: ${na.FieldText};
        box-shadow: 0 0 0 2px inset ${na.Field};
      }
    `));const fl=it.DataGridCell.compose({baseName:"data-grid-cell",template:it.dataGridCellTemplate,styles:bl});const $l=it.DataGridRow.compose({baseName:"data-grid-row",template:it.dataGridRowTemplate,styles:pl});const xl=it.DataGrid.compose({baseName:"data-grid",template:it.dataGridTemplate,styles:gl});const ml="Alt";const vl="AltGraph";const yl="CapsLock";const wl="Control";const kl="ArrowDown";const Fl="ArrowLeft";const Tl="ArrowRight";const Cl="ArrowUp";const Vl="Backspace";const Dl="Delete";const Sl="End";const jl="Enter";const Bl="Escape";const Ol="Home";const zl="Fn";const Ll="FnLock";const Hl="F2";const Nl="F3";const Al="F4";const Rl="F5";const Pl="F6";const Il="F7";const Ml="F8";const Gl="F9";const _l="F10";const El="F11";const ql="F12";const Wl="F13";const Ul="F14";const Xl="F15";const Zl="NumLock";const Yl="PageDown";const Jl="PageUp";const Kl="ScrollLock";const Ql="Shift";const es=" ";const ts="Tab";const os={ArrowDown:kl,ArrowLeft:Fl,ArrowRight:Tl,ArrowUp:Cl};class rs extends it.FoundationElement{}class ns extends((0,it.FormAssociated)(rs)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}const as={toView(e){if(e===null||e===undefined){return null}const t=new Date(e);return t.toString()==="Invalid Date"?null:`${t.getFullYear().toString().padStart(4,"0")}-${(t.getMonth()+1).toString().padStart(2,"0")}-${t.getDate().toString().padStart(2,"0")}`},fromView(e){if(e===null||e===undefined){return null}const t=new Date(e);return t.toString()==="Invalid Date"?null:t}};const is="Invalid Date";class ls extends ns{constructor(){super(...arguments);this.step=1;this.isUserInput=false}readOnlyChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.readOnly=this.readOnly;this.validate()}}autofocusChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.autofocus=this.autofocus;this.validate()}}listChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.setAttribute("list",this.list);this.validate()}}maxChanged(e,t){var o;this.max=t<((o=this.min)!==null&&o!==void 0?o:t)?this.min:t;this.value=this.getValidValue(this.value)}minChanged(e,t){var o;this.min=t>((o=this.max)!==null&&o!==void 0?o:t)?this.max:t;this.value=this.getValidValue(this.value)}get valueAsNumber(){return new Date(super.value).valueOf()}set valueAsNumber(e){this.value=new Date(e).toString()}get valueAsDate(){return new Date(super.value)}set valueAsDate(e){this.value=e.toString()}valueChanged(e,t){this.value=this.getValidValue(t);if(t!==this.value){return}if(this.control&&!this.isUserInput){this.control.value=this.value}super.valueChanged(e,this.value);if(e!==undefined&&!this.isUserInput){this.$emit("change")}this.isUserInput=false}getValidValue(e){var t,o;let r=new Date(e);if(r.toString()===is){r=""}else{r=r>((t=this.max)!==null&&t!==void 0?t:r)?this.max:r;r=r<((o=this.min)!==null&&o!==void 0?o:r)?this.min:r;r=`${r.getFullYear().toString().padStart(4,"0")}-${(r.getMonth()+1).toString().padStart(2,"0")}-${r.getDate().toString().padStart(2,"0")}`}return r}stepUp(){const e=864e5*this.step;const t=new Date(this.value);this.value=new Date(t.toString()!==is?t.valueOf()+e:0).toString()}stepDown(){const e=864e5*this.step;const t=new Date(this.value);this.value=new Date(t.toString()!==is?Math.max(t.valueOf()-e,0):0).toString()}connectedCallback(){super.connectedCallback();this.validate();this.control.value=this.value;if(this.autofocus){oa.DOM.queueUpdate((()=>{this.focus()}))}if(!this.appearance){this.appearance="outline"}}handleTextInput(){this.isUserInput=true;this.value=this.control.value}handleChange(){this.$emit("change")}handleKeyDown(e){const t=e.key;switch(t){case Cl:this.stepUp();return false;case kl:this.stepDown();return false}return true}handleBlur(){this.control.value=this.value}}gi([oa.attr],ls.prototype,"appearance",void 0);gi([(0,oa.attr)({attribute:"readonly",mode:"boolean"})],ls.prototype,"readOnly",void 0);gi([(0,oa.attr)({mode:"boolean"})],ls.prototype,"autofocus",void 0);gi([oa.attr],ls.prototype,"list",void 0);gi([(0,oa.attr)({converter:oa.nullableNumberConverter})],ls.prototype,"step",void 0);gi([(0,oa.attr)({converter:as})],ls.prototype,"max",void 0);gi([(0,oa.attr)({converter:as})],ls.prototype,"min",void 0);gi([oa.observable],ls.prototype,"defaultSlottedNodes",void 0);(0,it.applyMixins)(ls,it.StartEnd,it.DelegatesARIATextbox);const ss=oa.css`
  ${(0,it.display)("inline-block")} :host {
    font-family: ${Ht};
    outline: none;
    user-select: none;
  }

  .root {
    box-sizing: border-box;
    position: relative;
    display: flex;
    flex-direction: row;
    color: ${on};
    background: ${zr};
    border-radius: calc(${Pt} * 1px);
    border: calc(${Et} * 1px) solid ${_r};
    height: calc(${aa} * 1px);
  }

  .control {
    -webkit-appearance: none;
    font: inherit;
    background: transparent;
    border: 0;
    color: inherit;
    height: calc(100% - 4px);
    width: 100%;
    margin-top: auto;
    margin-bottom: auto;
    border: none;
    padding: 0 calc(${Mt} * 2px + 1px);
    font-size: ${Wt};
    line-height: ${Ut};
  }

  .control:hover,
  .control:${it.focusVisible},
  .control:disabled,
  .control:active {
    outline: none;
  }

  .label {
    display: block;
    color: ${on};
    cursor: pointer;
    font-size: ${Wt};
    line-height: ${Ut};
    margin-bottom: 4px;
  }

  .label__hidden {
    display: none;
    visibility: hidden;
  }

  .start,
  .end {
    margin: auto;
    fill: currentcolor;
  }

  ::slotted(svg) {
    /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
    width: 16px;
    height: 16px;
  }

  .start {
    margin-inline-start: 11px;
  }

  .end {
    margin-inline-end: 11px;
  }

  :host(:hover:not([disabled])) .root {
    background: ${Lr};
    border-color: ${Er};
  }

  :host(:active:not([disabled])) .root {
    background: ${Lr};
    border-color: ${qr};
  }

  :host(:focus-within:not([disabled])) .root {
    border-color: ${cr};
    box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px)
      ${cr};
  }

  :host([appearance='filled']) .root {
    background: ${Dr};
  }

  :host([appearance='filled']:hover:not([disabled])) .root {
    background: ${Sr};
  }

  :host([disabled]) .label,
  :host([readonly]) .label,
  :host([readonly]) .control,
  :host([disabled]) .control {
    cursor: ${it.disabledCursor};
  }

  :host([disabled]) {
    opacity: ${_t};
  }

  :host([disabled]) .control {
    border-color: ${nn};
  }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
    .root,
    :host([appearance='filled']) .root {
      forced-color-adjust: none;
      background: ${na.Field};
      border-color: ${na.FieldText};
    }
    :host(:hover:not([disabled])) .root,
    :host([appearance='filled']:hover:not([disabled])) .root,
    :host([appearance='filled']:hover) .root {
      background: ${na.Field};
      border-color: ${na.Highlight};
    }
    .start,
    .end {
      fill: currentcolor;
    }
    :host([disabled]) {
      opacity: 1;
    }
    :host([disabled]) .root,
    :host([appearance='filled']:hover[disabled]) .root {
      border-color: ${na.GrayText};
      background: ${na.Field};
    }
    :host(:focus-within:enabled) .root {
      border-color: ${na.Highlight};
      box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px)
        ${na.Highlight};
    }
    input::placeholder {
      color: ${na.GrayText};
    }
  `));const cs=(e,t)=>oa.css`
  ${ss}
`;const ds=(e,t)=>oa.html`
  <template class="${e=>e.readOnly?"readonly":""}">
    <label
      part="label"
      for="control"
      class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
    >
      <slot
        ${(0,oa.slotted)({property:"defaultSlottedNodes",filter:it.whitespaceFilter})}
      ></slot>
    </label>
    <div class="root" part="root">
      ${(0,it.startSlotTemplate)(e,t)}
      <input
        class="control"
        part="control"
        id="control"
        @input="${e=>e.handleTextInput()}"
        @change="${e=>e.handleChange()}"
        ?autofocus="${e=>e.autofocus}"
        ?disabled="${e=>e.disabled}"
        list="${e=>e.list}"
        ?readonly="${e=>e.readOnly}"
        ?required="${e=>e.required}"
        :value="${e=>e.value}"
        type="date"
        aria-atomic="${e=>e.ariaAtomic}"
        aria-busy="${e=>e.ariaBusy}"
        aria-controls="${e=>e.ariaControls}"
        aria-current="${e=>e.ariaCurrent}"
        aria-describedby="${e=>e.ariaDescribedby}"
        aria-details="${e=>e.ariaDetails}"
        aria-disabled="${e=>e.ariaDisabled}"
        aria-errormessage="${e=>e.ariaErrormessage}"
        aria-flowto="${e=>e.ariaFlowto}"
        aria-haspopup="${e=>e.ariaHaspopup}"
        aria-hidden="${e=>e.ariaHidden}"
        aria-invalid="${e=>e.ariaInvalid}"
        aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
        aria-label="${e=>e.ariaLabel}"
        aria-labelledby="${e=>e.ariaLabelledby}"
        aria-live="${e=>e.ariaLive}"
        aria-owns="${e=>e.ariaOwns}"
        aria-relevant="${e=>e.ariaRelevant}"
        aria-roledescription="${e=>e.ariaRoledescription}"
        ${(0,oa.ref)("control")}
      />
      ${(0,it.endSlotTemplate)(e,t)}
    </div>
  </template>
`;const hs=ls.compose({baseName:"date-field",styles:cs,template:ds,shadowOptions:{delegatesFocus:true}});const us=(e,t)=>oa.css`
    :host([hidden]) {
        display: none;
    }

    :host {
        --elevation: 14;
        --dialog-height: 480px;
        --dialog-width: 640px;
        display: block;
    }

    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.3);
        touch-action: none;
    }

    .positioning-region {
        display: flex;
        justify-content: center;
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        overflow: auto;
    }

    .control {
        ${Qi}
        margin-top: auto;
        margin-bottom: auto;
        width: var(--dialog-width);
        height: var(--dialog-height);
        background-color: ${rr};
        z-index: 1;
        border-radius: calc(${Pt} * 1px);
        border: calc(${Et} * 1px) solid transparent;
    }
`;const ps=it.Dialog.compose({baseName:"dialog",template:it.dialogTemplate,styles:us});const gs=(e,t)=>oa.css`
        ${(0,it.display)("block")} :host {
            box-sizing: content-box;
            height: 0;
            margin: calc(${Mt} * 1px) 0;
            border-top: calc(${Et} * 1px) solid ${dn};
            border-left: none;
        }

        :host([orientation="vertical"]) {
            height: 100%;
            margin: 0 calc(${Mt} * 1px);
            border-top: none;
            border-left: calc(${Et} * 1px) solid ${dn};
        }
    `;const bs=it.Divider.compose({baseName:"divider",template:it.dividerTemplate,styles:gs});const fs=(e,t)=>{const o=e.tagFor(it.ListboxOption);const r=e.name===e.tagFor(it.ListboxElement)?"":".listbox";return oa.css`
        ${!r?(0,it.display)("inline-flex"):""}

        :host ${r} {
            background: ${rr};
            border: calc(${Et} * 1px) solid ${nn};
            border-radius: calc(${Pt} * 1px);
            box-sizing: border-box;
            flex-direction: column;
            padding: calc(${Mt} * 1px) 0;
        }

        ${!r?oa.css`
            :host(:${it.focusVisible}:not([disabled])) {
                outline: none;
            }

            :host(:focus-within:not([disabled])) {
                border-color: ${Yr};
                box-shadow: 0 0 0
                    calc((${qt} - ${Et}) * 1px)
                    ${Yr} inset;
            }

            :host([disabled]) ::slotted(*) {
                cursor: ${it.disabledCursor};
                opacity: ${_t};
                pointer-events: none;
            }
        `:""}

        ${r||":host([size])"} {
            max-height: calc(
                (var(--size) * ${aa} + (${Mt} * ${Et} * 2)) * 1px
            );
            overflow-y: auto;
        }

        :host([size="0"]) ${r} {
            max-height: none;
        }
    `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                :host(:not([multiple]):${it.focusVisible}) ::slotted(${o}[aria-selected="true"]),
                :host([multiple]:${it.focusVisible}) ::slotted(${o}[aria-checked="true"]) {
                    border-color: ${na.ButtonText};
                    box-shadow: 0 0 0 calc(${qt} * 1px) inset ${na.HighlightText};
                }

                :host(:not([multiple]):${it.focusVisible}) ::slotted(${o}[aria-selected="true"]) {
                    background: ${na.Highlight};
                    color: ${na.HighlightText};
                    fill: currentcolor;
                }

                ::slotted(${o}[aria-selected="true"]:not([aria-checked="true"])) {
                    background: ${na.Highlight};
                    border-color: ${na.HighlightText};
                    color: ${na.HighlightText};
                }
            `))};const $s=it.ListboxElement.compose({baseName:"listbox",template:it.listboxTemplate,styles:fs});const xs=(e,t)=>oa.css`
        ${(0,it.display)("block")} :host {
            --elevation: 11;
            background: ${rr};
            border: calc(${Et} * 1px) solid transparent;
            ${Qi}
            margin: 0;
            border-radius: calc(${Pt} * 1px);
            padding: calc(${Mt} * 1px) 0;
            max-width: 368px;
            min-width: 64px;
        }

        :host([slot="submenu"]) {
            width: max-content;
            margin: 0 calc(${Mt} * 1px);
        }

        ::slotted(hr) {
            box-sizing: content-box;
            height: 0;
            margin: 0;
            border: none;
            border-top: calc(${Et} * 1px) solid ${dn};
        }
    `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                :host {
                    background: ${za.Canvas};
                    border-color: ${za.CanvasText};
                }
            `));const ms=it.Menu.compose({baseName:"menu",template:it.menuTemplate,styles:xs});const vs=(e,t)=>oa.css`
    ${(0,it.display)("grid")} :host {
      contain: layout;
      overflow: visible;
      font-family: ${Ht};
      outline: none;
      box-sizing: border-box;
      height: calc(${aa} * 1px);
      grid-template-columns: minmax(42px, auto) 1fr minmax(42px, auto);
      grid-template-rows: auto;
      justify-items: center;
      align-items: center;
      padding: 0;
      margin: 0 calc(${Mt} * 1px);
      white-space: nowrap;
      color: ${on};
      fill: currentcolor;
      cursor: pointer;
      font-size: ${Wt};
      line-height: ${Ut};
      border-radius: calc(${Pt} * 1px);
      border: calc(${qt} * 1px) solid transparent;
    }

    :host(:hover) {
      position: relative;
      z-index: 1;
    }

    :host(.indent-0) {
      grid-template-columns: auto 1fr minmax(42px, auto);
    }
    :host(.indent-0) .content {
      grid-column: 1;
      grid-row: 1;
      margin-inline-start: 10px;
    }
    :host(.indent-0) .expand-collapse-glyph-container {
      grid-column: 5;
      grid-row: 1;
    }
    :host(.indent-2) {
      grid-template-columns:
        minmax(42px, auto) minmax(42px, auto) 1fr minmax(42px, auto)
        minmax(42px, auto);
    }
    :host(.indent-2) .content {
      grid-column: 3;
      grid-row: 1;
      margin-inline-start: 10px;
    }
    :host(.indent-2) .expand-collapse-glyph-container {
      grid-column: 5;
      grid-row: 1;
    }
    :host(.indent-2) .start {
      grid-column: 2;
    }
    :host(.indent-2) .end {
      grid-column: 4;
    }

    :host(:${it.focusVisible}) {
      border-color: ${Yr};
      background: ${er};
      color: ${on};
    }

    :host(:hover) {
      background: ${er};
      color: ${on};
    }

    :host([aria-checked='true']),
    :host(:active),
    :host(.expanded) {
      background: ${Ko};
      color: ${on};
    }

    :host([disabled]) {
      cursor: ${it.disabledCursor};
      opacity: ${_t};
    }

    :host([disabled]:hover) {
      color: ${on};
      fill: currentcolor;
      background: ${Rr};
    }

    :host([disabled]:hover) .start,
    :host([disabled]:hover) .end,
    :host([disabled]:hover)::slotted(svg) {
      fill: ${on};
    }

    .expand-collapse-glyph {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
      fill: currentcolor;
    }

    .content {
      grid-column-start: 2;
      justify-self: start;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .start,
    .end {
      display: flex;
      justify-content: center;
    }

    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
    }

    :host(:hover) .start,
    :host(:hover) .end,
    :host(:hover)::slotted(svg),
    :host(:active) .start,
    :host(:active) .end,
    :host(:active)::slotted(svg) {
      fill: ${on};
    }

    :host(.indent-0[aria-haspopup='menu']) {
      display: grid;
      grid-template-columns: minmax(42px, auto) auto 1fr minmax(42px, auto) minmax(
          42px,
          auto
        );
      align-items: center;
      min-height: 32px;
    }

    :host(.indent-1[aria-haspopup='menu']),
    :host(.indent-1[role='menuitemcheckbox']),
    :host(.indent-1[role='menuitemradio']) {
      display: grid;
      grid-template-columns: minmax(42px, auto) auto 1fr minmax(42px, auto) minmax(
          42px,
          auto
        );
      align-items: center;
      min-height: 32px;
    }

    :host(.indent-2:not([aria-haspopup='menu'])) .end {
      grid-column: 5;
    }

    :host .input-container,
    :host .expand-collapse-glyph-container {
      display: none;
    }

    :host([aria-haspopup='menu']) .expand-collapse-glyph-container,
    :host([role='menuitemcheckbox']) .input-container,
    :host([role='menuitemradio']) .input-container {
      display: grid;
      margin-inline-end: 10px;
    }

    :host([aria-haspopup='menu']) .content,
    :host([role='menuitemcheckbox']) .content,
    :host([role='menuitemradio']) .content {
      grid-column-start: 3;
    }

    :host([aria-haspopup='menu'].indent-0) .content {
      grid-column-start: 1;
    }

    :host([aria-haspopup='menu']) .end,
    :host([role='menuitemcheckbox']) .end,
    :host([role='menuitemradio']) .end {
      grid-column-start: 4;
    }

    :host .expand-collapse,
    :host .checkbox,
    :host .radio {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      width: 20px;
      height: 20px;
      box-sizing: border-box;
      outline: none;
      margin-inline-start: 10px;
    }

    :host .checkbox,
    :host .radio {
      border: calc(${Et} * 1px) solid ${on};
    }

    :host([aria-checked='true']) .checkbox,
    :host([aria-checked='true']) .radio {
      background: ${ir};
      border-color: ${ir};
    }

    :host .checkbox {
      border-radius: calc(${Pt} * 1px);
    }

    :host .radio {
      border-radius: 999px;
    }

    :host .checkbox-indicator,
    :host .radio-indicator,
    :host .expand-collapse-indicator,
    ::slotted([slot='checkbox-indicator']),
    ::slotted([slot='radio-indicator']),
    ::slotted([slot='expand-collapse-indicator']) {
      display: none;
    }

    ::slotted([slot='end']:not(svg)) {
      margin-inline-end: 10px;
      color: ${en};
    }

    :host([aria-checked='true']) .checkbox-indicator,
    :host([aria-checked='true']) ::slotted([slot='checkbox-indicator']) {
      width: 100%;
      height: 100%;
      display: block;
      fill: ${ur};
      pointer-events: none;
    }

    :host([aria-checked='true']) .radio-indicator {
      position: absolute;
      top: 4px;
      left: 4px;
      right: 4px;
      bottom: 4px;
      border-radius: 999px;
      display: block;
      background: ${ur};
      pointer-events: none;
    }

    :host([aria-checked='true']) ::slotted([slot='radio-indicator']) {
      display: block;
      pointer-events: none;
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host {
        border-color: transparent;
        color: ${na.ButtonText};
        forced-color-adjust: none;
      }

      :host(:hover) {
        background: ${na.Highlight};
        color: ${na.HighlightText};
      }

      :host(:hover) .start,
      :host(:hover) .end,
      :host(:hover)::slotted(svg),
      :host(:active) .start,
      :host(:active) .end,
      :host(:active)::slotted(svg) {
        fill: ${na.HighlightText};
      }

      :host(.expanded) {
        background: ${na.Highlight};
        border-color: ${na.Highlight};
        color: ${na.HighlightText};
      }

      :host(:${it.focusVisible}) {
        background: ${na.Highlight};
        border-color: ${na.ButtonText};
        box-shadow: 0 0 0 calc(${qt} * 1px) inset
          ${na.HighlightText};
        color: ${na.HighlightText};
        fill: currentcolor;
      }

      :host([disabled]),
      :host([disabled]:hover),
      :host([disabled]:hover) .start,
      :host([disabled]:hover) .end,
      :host([disabled]:hover)::slotted(svg) {
        background: ${na.Canvas};
        color: ${na.GrayText};
        fill: currentcolor;
        opacity: 1;
      }

      :host .expanded-toggle,
      :host .checkbox,
      :host .radio {
        border-color: ${na.ButtonText};
        background: ${na.HighlightText};
      }

      :host([checked='true']) .checkbox,
      :host([checked='true']) .radio {
        background: ${na.HighlightText};
        border-color: ${na.HighlightText};
      }

      :host(:hover) .expanded-toggle,
            :host(:hover) .checkbox,
            :host(:hover) .radio,
            :host(:${it.focusVisible}) .expanded-toggle,
            :host(:${it.focusVisible}) .checkbox,
            :host(:${it.focusVisible}) .radio,
            :host([checked="true"]:hover) .checkbox,
            :host([checked="true"]:hover) .radio,
            :host([checked="true"]:${it.focusVisible}) .checkbox,
            :host([checked="true"]:${it.focusVisible}) .radio {
        border-color: ${na.HighlightText};
      }

      :host([aria-checked='true']) {
        background: ${na.Highlight};
        color: ${na.HighlightText};
      }

      :host([aria-checked='true']) .checkbox-indicator,
      :host([aria-checked='true']) ::slotted([slot='checkbox-indicator']),
      :host([aria-checked='true']) ::slotted([slot='radio-indicator']) {
        fill: ${na.Highlight};
      }

      :host([aria-checked='true']) .radio-indicator {
        background: ${na.Highlight};
      }

      ::slotted([slot='end']:not(svg)) {
        color: ${na.ButtonText};
      }

      :host(:hover) ::slotted([slot="end"]:not(svg)),
            :host(:${it.focusVisible}) ::slotted([slot="end"]:not(svg)) {
        color: ${na.HighlightText};
      }
    `),new Sn(oa.css`
        .expand-collapse-glyph {
          transform: rotate(0deg);
        }
      `,oa.css`
        .expand-collapse-glyph {
          transform: rotate(180deg);
        }
      `));const ys=it.MenuItem.compose({baseName:"menu-item",template:it.menuItemTemplate,styles:vs,checkboxIndicator:`\n      <svg\n        part="checkbox-indicator"\n        class="checkbox-indicator"\n        viewBox="0 0 20 20"\n        xmlns="http://www.w3.org/2000/svg"\n      >\n        <path\n          fill-rule="evenodd"\n          clip-rule="evenodd"\n          d="M8.143 12.6697L15.235 4.5L16.8 5.90363L8.23812 15.7667L3.80005 11.2556L5.27591 9.7555L8.143 12.6697Z"\n        />\n      </svg>\n    `,expandCollapseGlyph:`\n      <svg\n        viewBox="0 0 16 16"\n        xmlns="http://www.w3.org/2000/svg"\n        class="expand-collapse-glyph"\n        part="expand-collapse-glyph"\n      >\n        <path\n          d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"\n        />\n      </svg>\n    `,radioIndicator:`\n      <span part="radio-indicator" class="radio-indicator"></span>\n    `});const ws=(e,t)=>oa.css`
    ${(0,it.display)("inline-block")} :host {
        font-family: ${Ht};
        outline: none;
        user-select: none;
    }

    .root {
        box-sizing: border-box;
        position: relative;
        display: flex;
        flex-direction: row;
        color: ${on};
        background: ${zr};
        border-radius: calc(${Pt} * 1px);
        border: calc(${Et} * 1px) solid ${ir};
        height: calc(${La} * 1px);
        align-items: baseline;
    }

    .control {
        -webkit-appearance: none;
        font: inherit;
        background: transparent;
        border: 0;
        color: inherit;
        height: calc(100% - 4px);
        width: 100%;
        margin-top: auto;
        margin-bottom: auto;
        border: none;
        padding: 0 calc(${Mt} * 2px + 1px);
        font-size: ${Wt};
        line-height: ${Ut};
    }

    .control:hover,
    .control:${it.focusVisible},
    .control:disabled,
    .control:active {
        outline: none;
    }

    .controls {
        opacity: 0;
    }

    .label {
        display: block;
        color: ${on};
        cursor: pointer;
        font-size: ${Wt};
        line-height: ${Ut};
        margin-bottom: 4px;
    }

    .label__hidden {
        display: none;
        visibility: hidden;
    }

    .start,
    .control,
    .controls,
    .end {
        align-self: center;
    }

    .start,
    .end {
        margin: auto;
        fill: currentcolor;
    }

    .step-up-glyph,
    .step-down-glyph {
        display: block;
        padding: 4px 10px;
        cursor: pointer;
    }

    .step-up-glyph:before,
    .step-down-glyph:before {
        content: '';
        display: block;
        border: solid transparent 6px;
    }

    .step-up-glyph:before {
        border-bottom-color: ${on};
    }

    .step-down-glyph:before {
        border-top-color: ${on};
    }

    ::slotted(svg) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
    }

    .start {
        margin-inline-start: 11px;
    }

    .end {
        margin-inline-end: 11px;
    }

    :host(:hover:not([disabled])) .root {
        background: ${Lr};
        border-color: ${lr};
    }

    :host(:active:not([disabled])) .root {
        background: ${Lr};
        border-color: ${sr};
    }

    :host(:focus-within:not([disabled])) .root {
        border-color: ${Yr};
        box-shadow: 0 0 0 calc(${qt} * 1px) ${Yr} inset;
    }

    :host(:hover:not([disabled])) .controls,
    :host(:focus-within:not([disabled])) .controls {
        opacity: 1;
    }

    :host([appearance="filled"]) .root {
        background: ${Dr};
    }

    :host([appearance="filled"]:hover:not([disabled])) .root {
        background: ${Sr};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
        cursor: ${it.disabledCursor};
    }

    :host([disabled]) {
        opacity: ${_t};
    }

    :host([disabled]) .control {
        border-color: ${nn};
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                .root,
                :host([appearance="filled"]) .root {
                    forced-color-adjust: none;
                    background: ${za.Field};
                    border-color: ${za.FieldText};
                }
                :host(:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover) .root {
                    background: ${za.Field};
                    border-color: ${za.Highlight};
                }
                .start,
                .end {
                    fill: currentcolor;
                }
                :host([disabled]) {
                    opacity: 1;
                }
                :host([disabled]) .root,
                :host([appearance="filled"]:hover[disabled]) .root {
                    border-color: ${za.GrayText};
                    background: ${za.Field};
                }
                :host(:focus-within:enabled) .root {
                    border-color: ${za.Highlight};
                    box-shadow: 0 0 0 1px ${za.Highlight} inset;
                }
                input::placeholder {
                    color: ${za.GrayText};
                }
            `));class ks extends it.NumberField{constructor(){super(...arguments);this.appearance="outline"}}pa([oa.attr],ks.prototype,"appearance",void 0);const Fs=ks.compose({baseName:"number-field",baseClass:it.NumberField,styles:ws,template:it.numberFieldTemplate,shadowOptions:{delegatesFocus:true},stepDownGlyph:`\n        <span class="step-down-glyph" part="step-down-glyph"></span>\n    `,stepUpGlyph:`\n        <span class="step-up-glyph" part="step-up-glyph"></span>\n    `});const Ts=(e,t)=>oa.css`
  ${ss}

  .controls {
    opacity: 0;
  }

  .step-up-glyph,
  .step-down-glyph {
    display: block;
    padding: 4px 10px;
    cursor: pointer;
  }

  .step-up-glyph:before,
  .step-down-glyph:before {
    content: '';
    display: block;
    border: solid transparent 6px;
  }

  .step-up-glyph:before {
    border-bottom-color: ${on};
  }

  .step-down-glyph:before {
    border-top-color: ${on};
  }

  :host(:hover:not([disabled])) .controls,
  :host(:focus-within:not([disabled])) .controls {
    opacity: 1;
  }
`;const Cs=ks.compose({baseName:"number-field",baseClass:it.NumberField,styles:Ts,template:it.numberFieldTemplate,shadowOptions:{delegatesFocus:true},stepDownGlyph:`\n        <span class="step-down-glyph" part="step-down-glyph"></span>\n    `,stepUpGlyph:`\n        <span class="step-up-glyph" part="step-up-glyph"></span>\n    `});const Vs=(e,t)=>oa.css`
    ${(0,it.display)("inline-flex")} :host {
      align-items: center;
      font-family: ${Ht};
      border-radius: calc(${Pt} * 1px);
      border: calc(${qt} * 1px) solid transparent;
      box-sizing: border-box;
      color: ${on};
      cursor: pointer;
      flex: 0 0 auto;
      fill: currentcolor;
      font-size: ${Wt};
      height: calc(${aa} * 1px);
      line-height: ${Ut};
      margin: 0 calc(${Mt} * 1px);
      outline: none;
      overflow: hidden;
      padding: 0 calc(${Mt} * 2.25px);
      user-select: none;
      white-space: nowrap;
    }

    /* TODO should we use outline instead of background for focus to support multi-selection */
    :host(:${it.focusVisible}) {
      background: ${cr};
      color: ${br};
    }

    :host([aria-selected='true']) {
      background: ${ir};
      color: ${ur};
    }

    :host(:hover) {
      background: ${lr};
      color: ${pr};
    }

    :host(:active) {
      background: ${sr};
      color: ${gr};
    }

    :host(:not([aria-selected='true']):hover),
    :host(:not([aria-selected='true']):active) {
      background: ${Sr};
      color: ${on};
    }

    :host([disabled]) {
      cursor: ${it.disabledCursor};
      opacity: ${_t};
    }

    :host([disabled]:hover) {
      background-color: inherit;
    }

    .content {
      grid-column-start: 2;
      justify-self: start;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .start,
    .end,
    ::slotted(svg) {
      display: flex;
    }

    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      height: calc(${Mt} * 4px);
      width: calc(${Mt} * 4px);
    }

    ::slotted([slot='end']) {
      margin-inline-start: 1ch;
    }

    ::slotted([slot='start']) {
      margin-inline-end: 1ch;
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host {
        border-color: transparent;
        forced-color-adjust: none;
        color: ${na.ButtonText};
        fill: currentcolor;
      }

      :host(:not([aria-selected='true']):hover),
      :host([aria-selected='true']) {
        background: ${na.Highlight};
        color: ${na.HighlightText};
      }

      :host([disabled]),
      :host([disabled]:not([aria-selected='true']):hover) {
        background: ${na.Canvas};
        color: ${na.GrayText};
        fill: currentcolor;
        opacity: 1;
      }
    `));const Ds=it.ListboxOption.compose({baseName:"option",template:it.listboxOptionTemplate,styles:Vs});const Ss=(e,t)=>oa.css`
        ${(0,it.display)("flex")} :host {
            align-items: center;
            outline: none;
            height: calc(${Mt} * 1px);
            margin: calc(${Mt} * 1px) 0;
        }

        .progress {
            background-color: ${Dr};
            border-radius: calc(${Mt} * 1px);
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            position: relative;
        }

        .determinate {
            background-color: ${kr};
            border-radius: calc(${Mt} * 1px);
            height: 100%;
            transition: all 0.2s ease-in-out;
            display: flex;
        }

        .indeterminate {
            height: 100%;
            border-radius: calc(${Mt} * 1px);
            display: flex;
            width: 100%;
            position: relative;
            overflow: hidden;
        }

        .indeterminate-indicator-1 {
            position: absolute;
            opacity: 0;
            height: 100%;
            background-color: ${kr};
            border-radius: calc(${Mt} * 1px);
            animation-timing-function: cubic-bezier(0.4, 0, 0.6, 1);
            width: 40%;
            animation: indeterminate-1 2s infinite;
        }

        .indeterminate-indicator-2 {
            position: absolute;
            opacity: 0;
            height: 100%;
            background-color: ${kr};
            border-radius: calc(${Mt} * 1px);
            animation-timing-function: cubic-bezier(0.4, 0, 0.6, 1);
            width: 60%;
            animation: indeterminate-2 2s infinite;
        }

        :host([paused]) .indeterminate-indicator-1,
        :host([paused]) .indeterminate-indicator-2 {
            animation-play-state: paused;
            background-color: ${Dr};
        }

        :host([paused]) .determinate {
            background-color: ${en};
        }

        @keyframes indeterminate-1 {
            0% {
                opacity: 1;
                transform: translateX(-100%);
            }
            70% {
                opacity: 1;
                transform: translateX(300%);
            }
            70.01% {
                opacity: 0;
            }
            100% {
                opacity: 0;
                transform: translateX(300%);
            }
        }

        @keyframes indeterminate-2 {
            0% {
                opacity: 0;
                transform: translateX(-150%);
            }
            29.99% {
                opacity: 0;
            }
            30% {
                opacity: 1;
                transform: translateX(-150%);
            }
            100% {
                transform: translateX(166.66%);
                opacity: 1;
            }
        }
    `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                .progress {
                    forced-color-adjust: none;
                    background-color: ${za.Field};
                    box-shadow: 0 0 0 1px inset ${za.FieldText};
                }
                .determinate,
                .indeterminate-indicator-1,
                .indeterminate-indicator-2 {
                    forced-color-adjust: none;
                    background-color: ${za.FieldText};
                }
                :host([paused]) .determinate,
                :host([paused]) .indeterminate-indicator-1,
                :host([paused]) .indeterminate-indicator-2 {
                    background-color: ${za.GrayText};
                }
            `));const js=it.BaseProgress.compose({baseName:"progress",template:it.progressTemplate,styles:Ss,indeterminateIndicator1:`\n        <span class="indeterminate-indicator-1" part="indeterminate-indicator-1"></span>\n    `,indeterminateIndicator2:`\n        <span class="indeterminate-indicator-2" part="indeterminate-indicator-2"></span>\n    `});const Bs=(e,t)=>oa.css`
        ${(0,it.display)("flex")} :host {
            align-items: center;
            outline: none;
            height: calc(${La} * 1px);
            width: calc(${La} * 1px);
            margin: calc(${La} * 1px) 0;
        }

        .progress {
            height: 100%;
            width: 100%;
        }

        .background {
            stroke: ${Dr};
            fill: none;
            stroke-width: 2px;
        }

        .determinate {
            stroke: ${kr};
            fill: none;
            stroke-width: 2px;
            stroke-linecap: round;
            transform-origin: 50% 50%;
            transform: rotate(-90deg);
            transition: all 0.2s ease-in-out;
        }

        .indeterminate-indicator-1 {
            stroke: ${kr};
            fill: none;
            stroke-width: 2px;
            stroke-linecap: round;
            transform-origin: 50% 50%;
            transform: rotate(-90deg);
            transition: all 0.2s ease-in-out;
            animation: spin-infinite 2s linear infinite;
        }

        :host([paused]) .indeterminate-indicator-1 {
            animation-play-state: paused;
            stroke: ${Dr};
        }

        :host([paused]) .determinate {
            stroke: ${en};
        }

        @keyframes spin-infinite {
            0% {
                stroke-dasharray: 0.01px 43.97px;
                transform: rotate(0deg);
            }
            50% {
                stroke-dasharray: 21.99px 21.99px;
                transform: rotate(450deg);
            }
            100% {
                stroke-dasharray: 0.01px 43.97px;
                transform: rotate(1080deg);
            }
        }
    `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                .indeterminate-indicator-1,
                .determinate {
                    stroke: ${za.FieldText};
                }
                .background {
                    stroke: ${za.Field};
                }
                :host([paused]) .indeterminate-indicator-1 {
                    stroke: ${za.Field};
                }
                :host([paused]) .determinate {
                    stroke: ${za.GrayText};
                }
            `));const Os=it.BaseProgress.compose({baseName:"progress-ring",template:it.progressRingTemplate,styles:Bs,indeterminateIndicator:`\n        <svg class="progress" part="progress" viewBox="0 0 16 16">\n            <circle\n                class="background"\n                part="background"\n                cx="8px"\n                cy="8px"\n                r="7px"\n            ></circle>\n            <circle\n                class="indeterminate-indicator-1"\n                part="indeterminate-indicator-1"\n                cx="8px"\n                cy="8px"\n                r="7px"\n            ></circle>\n        </svg>\n    `});const zs=(e,t)=>oa.css`
    ${(0,it.display)("inline-flex")} :host {
      --input-size: calc((${aa} / 2) + ${Mt});
      align-items: center;
      outline: none;
      margin: calc(${Mt} * 1px) 0;
      /* Chromium likes to select label text or the default slot when
         the radio is clicked. Maybe there is a better solution here? */
      user-select: none;
      position: relative;
      flex-direction: row;
      transition: all 0.2s ease-in-out;
    }

    .control {
      position: relative;
      width: calc((${aa} / 2 + ${Mt}) * 1px);
      height: calc((${aa} / 2 + ${Mt}) * 1px);
      box-sizing: border-box;
      border-radius: 999px;
      border: calc(${Et} * 1px) solid ${nn};
      background: ${zr};
      outline: none;
      cursor: pointer;
    }

    .label {
      font-family: ${Ht};
      color: ${on};
      /* Need to discuss with Brian how HorizontalSpacingNumber can work.
            https://github.com/microsoft/fast/issues/2766 */
      padding-inline-start: calc(${Mt} * 2px + 2px);
      margin-inline-end: calc(${Mt} * 2px + 2px);
      cursor: pointer;
      font-size: ${Wt};
      line-height: ${Ut};
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    .control,
    .checked-indicator {
      flex-shrink: 0;
    }

    .checked-indicator {
      position: absolute;
      top: 5px;
      left: 5px;
      right: 5px;
      bottom: 5px;
      border-radius: 999px;
      display: inline-block;
      background: ${ur};
      fill: ${ur};
      opacity: 0;
      pointer-events: none;
    }

    :host(:not([disabled])) .control:hover {
      background: ${Lr};
      border-color: ${an};
    }

    :host(:not([disabled])) .control:active {
      background: ${Hr};
      border-color: ${ln};
    }

    :host(:${it.focusVisible}) .control {
      outline: solid calc(${qt} * 1px) ${cr};
    }

    :host([aria-checked='true']) .control {
      background: ${ir};
      border: calc(${Et} * 1px) solid ${ir};
    }

    :host([aria-checked='true']:not([disabled])) .control:hover {
      background: ${lr};
      border: calc(${Et} * 1px) solid ${lr};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:hover
      .checked-indicator {
      background: ${pr};
      fill: ${pr};
    }

    :host([aria-checked='true']:not([disabled])) .control:active {
      background: ${sr};
      border: calc(${Et} * 1px) solid ${sr};
    }

    :host([aria-checked='true']:not([disabled]))
      .control:active
      .checked-indicator {
      background: ${gr};
      fill: ${gr};
    }

    :host([aria-checked="true"]:${it.focusVisible}:not([disabled])) .control {
      outline-offset: 2px;
      outline: solid calc(${qt} * 1px) ${cr};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${it.disabledCursor};
    }

    :host([aria-checked='true']) .checked-indicator {
      opacity: 1;
    }

    :host([disabled]) {
      opacity: ${_t};
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      .control,
      :host([aria-checked='true']:not([disabled])) .control {
        forced-color-adjust: none;
        border-color: ${na.FieldText};
        background: ${na.Field};
      }
      :host(:not([disabled])) .control:hover {
        border-color: ${na.Highlight};
        background: ${na.Field};
      }
      :host([aria-checked='true']:not([disabled])) .control:hover,
      :host([aria-checked='true']:not([disabled])) .control:active {
        border-color: ${na.Highlight};
        background: ${na.Highlight};
      }
      :host([aria-checked='true']) .checked-indicator {
        background: ${na.Highlight};
        fill: ${na.Highlight};
      }
      :host([aria-checked='true']:not([disabled]))
        .control:hover
        .checked-indicator,
      :host([aria-checked='true']:not([disabled]))
        .control:active
        .checked-indicator {
        background: ${na.HighlightText};
        fill: ${na.HighlightText};
      }
      :host(:${it.focusVisible}) .control {
        border-color: ${na.Highlight};
        outline-offset: 2px;
        outline: solid calc(${qt} * 1px) ${na.FieldText};
      }
      :host([aria-checked="true"]:${it.focusVisible}:not([disabled])) .control {
        border-color: ${na.Highlight};
        outline: solid calc(${qt} * 1px) ${na.FieldText};
      }
      :host([disabled]) {
        forced-color-adjust: none;
        opacity: 1;
      }
      :host([disabled]) .label {
        color: ${na.GrayText};
      }
      :host([disabled]) .control,
      :host([aria-checked='true'][disabled]) .control:hover,
      .control:active {
        background: ${na.Field};
        border-color: ${na.GrayText};
      }
      :host([disabled]) .checked-indicator,
      :host([aria-checked='true'][disabled]) .control:hover .checked-indicator {
        fill: ${na.GrayText};
        background: ${na.GrayText};
      }
    `));const Ls=it.Radio.compose({baseName:"radio",template:it.radioTemplate,styles:zs,checkedIndicator:`\n    <div part="checked-indicator" class="checked-indicator"></div>\n  `});const Hs=(e,t)=>oa.css`
    ${(0,it.display)("flex")} :host {
        align-items: flex-start;
        margin: calc(${Mt} * 1px) 0;
        flex-direction: column;
    }
    .positioning-region {
        display: flex;
        flex-wrap: wrap;
    }
    :host([orientation="vertical"]) .positioning-region {
        flex-direction: column;
    }
    :host([orientation="horizontal"]) .positioning-region {
        flex-direction: row;
    }
`;const Ns=it.RadioGroup.compose({baseName:"radio-group",template:it.radioGroupTemplate,styles:Hs});const As=it.DesignToken.create("clear-button-hover").withDefault((e=>{const t=Ar.getValueFor(e);const o=Vr.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).hover}));const Rs=it.DesignToken.create("clear-button-active").withDefault((e=>{const t=Ar.getValueFor(e);const o=Vr.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).active}));const Ps=(e,t)=>oa.css`
    ${(0,it.display)("inline-block")} :host {
        font-family: ${Ht};
        outline: none;
        user-select: none;
    }

    .root {
        box-sizing: border-box;
        position: relative;
        display: flex;
        flex-direction: row;
        color: ${on};
        background: ${zr};
        border-radius: calc(${Pt} * 1px);
        border: calc(${Et} * 1px) solid ${ir};
        height: calc(${La} * 1px);
        align-items: baseline;
    }

    .control {
        -webkit-appearance: none;
        font: inherit;
        background: transparent;
        border: 0;
        color: inherit;
        height: calc(100% - 4px);
        width: 100%;
        margin-top: auto;
        margin-bottom: auto;
        border: none;
        padding: 0 calc(${Mt} * 2px + 1px);
        font-size: ${Wt};
        line-height: ${Ut};
    }

    .control::-webkit-search-cancel-button {
        -webkit-appearance: none;
    }

    .control:hover,
    .control:${it.focusVisible},
    .control:disabled,
    .control:active {
        outline: none;
    }

    .clear-button {
        height: calc(100% - 2px);
        opacity: 0;
        margin: 1px;
        background: transparent;
        color: ${on};
        fill: currentcolor;
        border: none;
        border-radius: calc(${Pt} * 1px);
        min-width: calc(${La} * 1px);
        font-size: ${Wt};
        line-height: ${Ut};
        outline: none;
        font-family: ${Ht};
        padding: 0 calc((10 + (${Mt} * 2 * ${It})) * 1px);
    }

    .clear-button:hover {
        background: ${Pr};
    }

    .clear-button:active {
        background: ${Ir};
    }

    :host([appearance="filled"]) .clear-button:hover {
        background: ${As};
    }

    :host([appearance="filled"]) .clear-button:active {
        background: ${Rs};
    }

    .input-wrapper {
        display: flex;
        position: relative;
        width: 100%;
        height: 100%;
    }

    .label {
        display: block;
        color: ${on};
        cursor: pointer;
        font-size: ${Wt};
        line-height: ${Ut};
        margin-bottom: 4px;
    }

    .label__hidden {
        display: none;
        visibility: hidden;
    }

    .input-wrapper,
    .start,
    .end {
        align-self: center;
    }

    .start,
    .end {
        display: flex;
        margin: 1px;
        fill: currentcolor;
    }

    ::slotted([slot="end"]) {
        height: 100%
    }

    .end {
        margin-inline-end: 1px;
        height: calc(100% - 2px);
    }

    ::slotted(svg) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
        margin-inline-end: 11px;
        margin-inline-start: 11px;
        margin-top: auto;
        margin-bottom: auto;
    }

    :host(:hover:not([disabled])) .root {
        background: ${Lr};
        border-color: ${lr};
    }

    :host(:active:not([disabled])) .root {
        background: ${Lr};
        border-color: ${sr};
    }

    :host(:focus-within:not([disabled])) .root {
        border-color: ${Yr};
        box-shadow: 0 0 0 1px ${Yr} inset;
    }

    .clear-button__hidden {
        opacity: 0;
    }

    :host(:hover:not([disabled], [readOnly])) .clear-button,
    :host(:active:not([disabled], [readOnly])) .clear-button,
    :host(:focus-within:not([disabled], [readOnly])) .clear-button {
        opacity: 1;
    }

    :host(:hover:not([disabled], [readOnly])) .clear-button__hidden,
    :host(:active:not([disabled], [readOnly])) .clear-button__hidden,
    :host(:focus-within:not([disabled], [readOnly])) .clear-button__hidden {
        opacity: 0;
    }

    :host([appearance="filled"]) .root {
        background: ${rr};
    }

    :host([appearance="filled"]:hover:not([disabled])) .root {
        background: ${Sr};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
        cursor: ${it.disabledCursor};
    }

    :host([disabled]) {
        opacity: ${_t};
    }

    :host([disabled]) .control {
        border-color: ${nn};
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                .root,
                :host([appearance="filled"]) .root {
                    forced-color-adjust: none;
                    background: ${za.Field};
                    border-color: ${za.FieldText};
                }
                :host(:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover) .root {
                    background: ${za.Field};
                    border-color: ${za.Highlight};
                }
                .start,
                .end {
                    fill: currentcolor;
                }
                :host([disabled]) {
                    opacity: 1;
                }
                :host([disabled]) .root,
                :host([appearance="filled"]:hover[disabled]) .root {
                    border-color: ${za.GrayText};
                    background: ${za.Field};
                }
                :host(:focus-within:enabled) .root {
                    border-color: ${za.Highlight};
                    box-shadow: 0 0 0 1px ${za.Highlight} inset;
                }
                input::placeholder {
                    color: ${za.GrayText};
                }
            `));class Is extends it.Search{constructor(){super(...arguments);this.appearance="outline"}}pa([oa.attr],Is.prototype,"appearance",void 0);const Ms=Is.compose({baseName:"search",baseClass:it.Search,template:it.searchTemplate,styles:Ps,shadowOptions:{delegatesFocus:true}});const Gs=null&&styles;const _s=it.DesignToken.create("clear-button-hover").withDefault((e=>{const t=Ar.getValueFor(e);const o=Vr.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).hover}));const Es=it.DesignToken.create("clear-button-active").withDefault((e=>{const t=Ar.getValueFor(e);const o=Vr.getValueFor(e);return t.evaluate(e,o.evaluate(e).hover).active}));const qs=(e,t)=>oa.css`
  ${ss}

  .control {
    padding: 0;
    padding-inline-start: calc(${Mt} * 2px + 1px);
    padding-inline-end: calc(
      (${Mt} * 2px) + (${aa} * 1px) + 1px
    );
  }

  .control::-webkit-search-cancel-button {
    -webkit-appearance: none;
  }

  .control:hover,
    .control:${it.focusVisible},
    .control:disabled,
    .control:active {
    outline: none;
  }

  .clear-button {
    height: calc(100% - 2px);
    opacity: 0;
    margin: 1px;
    background: transparent;
    color: ${on};
    fill: currentcolor;
    border: none;
    border-radius: calc(${Pt} * 1px);
    min-width: calc(${aa} * 1px);
    font-size: ${Wt};
    line-height: ${Ut};
    outline: none;
    font-family: ${Ht};
    padding: 0 calc((10 + (${Mt} * 2 * ${It})) * 1px);
  }

  .clear-button:hover {
    background: ${Pr};
  }

  .clear-button:active {
    background: ${Ir};
  }

  :host([appearance='filled']) .clear-button:hover {
    background: ${_s};
  }

  :host([appearance='filled']) .clear-button:active {
    background: ${Es};
  }

  .input-wrapper {
    display: flex;
    position: relative;
    width: 100%;
  }

  .start,
  .end {
    display: flex;
    margin: 1px;
  }

  ::slotted([slot='end']) {
    height: 100%;
  }

  .end {
    margin-inline-end: 1px;
  }

  ::slotted(svg) {
    /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
    margin-inline-end: 11px;
    margin-inline-start: 11px;
    margin-top: auto;
    margin-bottom: auto;
  }

  .clear-button__hidden {
    opacity: 0;
  }

  :host(:hover:not([disabled], [readOnly])) .clear-button,
  :host(:active:not([disabled], [readOnly])) .clear-button,
  :host(:focus-within:not([disabled], [readOnly])) .clear-button {
    opacity: 1;
  }

  :host(:hover:not([disabled], [readOnly])) .clear-button__hidden,
  :host(:active:not([disabled], [readOnly])) .clear-button__hidden,
  :host(:focus-within:not([disabled], [readOnly])) .clear-button__hidden {
    opacity: 0;
  }
`;const Ws=Is.compose({baseName:"search",baseClass:it.Search,template:it.searchTemplate,styles:qs,shadowOptions:{delegatesFocus:true}});class Us extends it.Select{connectedCallback(){super.connectedCallback();this.setAutoWidth()}slottedOptionsChanged(e,t){super.slottedOptionsChanged(e,t);this.setAutoWidth()}autoWidthChanged(e,t){if(t){this.setAutoWidth()}else{this.style.removeProperty("width")}}setAutoWidth(){if(!this.autoWidth||!this.isConnected){return}let e=this.listbox.getBoundingClientRect().width;if(e===0&&this.listbox.hidden){Object.assign(this.listbox.style,{visibility:"hidden"});this.listbox.removeAttribute("hidden");e=this.listbox.getBoundingClientRect().width;this.listbox.setAttribute("hidden","");this.listbox.style.removeProperty("visibility")}if(e>0){Object.assign(this.style,{width:`${e}px`})}}}gi([(0,oa.attr)({attribute:"autowidth",mode:"boolean"})],Us.prototype,"autoWidth",void 0);gi([(0,oa.attr)({attribute:"minimal",mode:"boolean"})],Us.prototype,"minimal",void 0);const Xs=Us.compose({baseName:"select",baseClass:it.Select,template:it.selectTemplate,styles:cl,indicator:`\n        <svg\n            class="select-indicator"\n            part="select-indicator"\n            viewBox="0 0 12 7"\n            xmlns="http://www.w3.org/2000/svg"\n        >\n            <path\n                d="M11.85.65c.2.2.2.5 0 .7L6.4 6.84a.55.55 0 01-.78 0L.14 1.35a.5.5 0 11.71-.7L6 5.8 11.15.65c.2-.2.5-.2.7 0z"\n            />\n        </svg>\n    `});const Zs=(e,t)=>oa.css`
    :host([hidden]) {
      display: none;
    }

    ${(0,it.display)("inline-grid")} :host {
      --thumb-size: calc(${aa} * 0.5 - ${Mt});
      --thumb-translate: calc(
        var(--thumb-size) * -0.5 + var(--track-width) / 2
      );
      --track-overhang: calc((${Mt} / 2) * -1);
      --track-width: ${Mt};
      --jp-slider-height: calc(var(--thumb-size) * 10);
      align-items: center;
      width: 100%;
      margin: calc(${Mt} * 1px) 0;
      user-select: none;
      box-sizing: border-box;
      border-radius: calc(${Pt} * 1px);
      outline: none;
      cursor: pointer;
    }
    :host([orientation='horizontal']) .positioning-region {
      position: relative;
      margin: 0 8px;
      display: grid;
      grid-template-rows: calc(var(--thumb-size) * 1px) 1fr;
    }
    :host([orientation='vertical']) .positioning-region {
      position: relative;
      margin: 0 8px;
      display: grid;
      height: 100%;
      grid-template-columns: calc(var(--thumb-size) * 1px) 1fr;
    }

    :host(:${it.focusVisible}) .thumb-cursor {
      box-shadow:
        0 0 0 2px ${rr},
        0 0 0 calc((2 + ${qt}) * 1px) ${cr};
    }

    .thumb-container {
      position: absolute;
      height: calc(var(--thumb-size) * 1px);
      width: calc(var(--thumb-size) * 1px);
      transition: all 0.2s ease;
      color: ${on};
      fill: currentcolor;
    }
    .thumb-cursor {
      border: none;
      width: calc(var(--thumb-size) * 1px);
      height: calc(var(--thumb-size) * 1px);
      background: ${on};
      border-radius: calc(${Pt} * 1px);
    }
    .thumb-cursor:hover {
      background: ${on};
      border-color: ${an};
    }
    .thumb-cursor:active {
      background: ${on};
    }
    :host([orientation='horizontal']) .thumb-container {
      transform: translateX(calc(var(--thumb-size) * 0.5px))
        translateY(calc(var(--thumb-translate) * 1px));
    }
    :host([orientation='vertical']) .thumb-container {
      transform: translateX(calc(var(--thumb-translate) * 1px))
        translateY(calc(var(--thumb-size) * 0.5px));
    }
    :host([orientation='horizontal']) {
      min-width: calc(var(--thumb-size) * 1px);
    }
    :host([orientation='horizontal']) .track {
      right: calc(var(--track-overhang) * 1px);
      left: calc(var(--track-overhang) * 1px);
      align-self: start;
      height: calc(var(--track-width) * 1px);
    }
    :host([orientation='vertical']) .track {
      top: calc(var(--track-overhang) * 1px);
      bottom: calc(var(--track-overhang) * 1px);
      width: calc(var(--track-width) * 1px);
      height: 100%;
    }
    .track {
      background: ${nn};
      position: absolute;
      border-radius: calc(${Pt} * 1px);
    }
    :host([orientation='vertical']) {
      height: calc(var(--jp-slider-height) * 1px);
      min-height: calc(var(--thumb-size) * 1px);
      min-width: calc(${Mt} * 20px);
    }
    :host([disabled]),
    :host([readonly]) {
      cursor: ${it.disabledCursor};
    }
    :host([disabled]) {
      opacity: ${_t};
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      .thumb-cursor {
        forced-color-adjust: none;
        border-color: ${na.FieldText};
        background: ${na.FieldText};
      }
      .thumb-cursor:hover,
      .thumb-cursor:active {
        background: ${na.Highlight};
      }
      .track {
        forced-color-adjust: none;
        background: ${na.FieldText};
      }
      :host(:${it.focusVisible}) .thumb-cursor {
        border-color: ${na.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host([disabled]) .track,
      :host([disabled]) .thumb-cursor {
        forced-color-adjust: none;
        background: ${na.GrayText};
      }

      :host(:${it.focusVisible}) .thumb-cursor {
        background: ${na.Highlight};
        border-color: ${na.Highlight};
        box-shadow:
          0 0 0 2px ${na.Field},
          0 0 0 4px ${na.FieldText};
      }
    `));const Ys=it.Slider.compose({baseName:"slider",template:it.sliderTemplate,styles:Zs,thumb:`\n        <div class="thumb-cursor"></div>\n    `});var Js=o(62899);const Ks=oa.css`
    :host {
        align-self: start;
        grid-row: 2;
        margin-top: -2px;
        height: calc((${La} / 2 + ${Mt}) * 1px);
        width: auto;
    }
    .container {
        grid-template-rows: auto auto;
        grid-template-columns: 0;
    }
    .label {
        margin: 2px 0;
    }
`;const Qs=oa.css`
    :host {
        justify-self: start;
        grid-column: 2;
        margin-left: 2px;
        height: auto;
        width: calc((${La} / 2 + ${Mt}) * 1px);
    }
    .container {
        grid-template-columns: auto auto;
        grid-template-rows: 0;
        min-width: calc(var(--thumb-size) * 1px);
        height: calc(var(--thumb-size) * 1px);
    }
    .mark {
        transform: rotate(90deg);
        align-self: center;
    }
    .label {
        margin-left: calc((${Mt} / 2) * 3px);
        align-self: center;
    }
`;const ec=(e,t)=>oa.css`
        ${(0,it.display)("block")} :host {
            font-family: ${Ht};
            color: ${on};
            fill: currentcolor;
        }
        .root {
            position: absolute;
            display: grid;
        }
        .container {
            display: grid;
            justify-self: center;
        }
        .label {
            justify-self: center;
            align-self: center;
            white-space: nowrap;
            max-width: 30px;
        }
        .mark {
            width: calc((${Mt} / 4) * 1px);
            height: calc(${La} * 0.25 * 1px);
            background: ${nn};
            justify-self: center;
        }
        :host(.disabled) {
            opacity: ${_t};
        }
    `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                .mark {
                    forced-color-adjust: none;
                    background: ${za.FieldText};
                }
                :host(.disabled) {
                    forced-color-adjust: none;
                    opacity: 1;
                }
                :host(.disabled) .label {
                    color: ${za.GrayText};
                }
                :host(.disabled) .mark {
                    background: ${za.GrayText};
                }
            `));class tc extends it.SliderLabel{sliderOrientationChanged(){if(this.sliderOrientation===Js.i.horizontal){this.$fastController.addStyles(Ks);this.$fastController.removeStyles(Qs)}else{this.$fastController.addStyles(Qs);this.$fastController.removeStyles(Ks)}}}const oc=tc.compose({baseName:"slider-label",baseClass:it.SliderLabel,template:it.sliderLabelTemplate,styles:ec});const rc=tc.compose({baseName:"slider-label",baseClass:it.SliderLabel,template:it.sliderLabelTemplate,styles:ec});const nc=(e,t)=>oa.css`
    :host([hidden]) {
      display: none;
    }

    ${(0,it.display)("inline-flex")} :host {
      align-items: center;
      outline: none;
      font-family: ${Ht};
      margin: calc(${Mt} * 1px) 0;
      ${""} user-select: none;
    }

    :host([disabled]) {
      opacity: ${_t};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .switch,
    :host([disabled]) .switch {
      cursor: ${it.disabledCursor};
    }

    .switch {
      position: relative;
      outline: none;
      box-sizing: border-box;
      width: calc(${aa} * 1px);
      height: calc((${aa} / 2 + ${Mt}) * 1px);
      background: ${zr};
      border-radius: calc(${Pt} * 1px);
      border: calc(${Et} * 1px) solid ${nn};
    }

    .switch:hover {
      background: ${Lr};
      border-color: ${an};
      cursor: pointer;
    }

    host([disabled]) .switch:hover,
    host([readonly]) .switch:hover {
      background: ${Lr};
      border-color: ${an};
      cursor: ${it.disabledCursor};
    }

    :host(:not([disabled])) .switch:active {
      background: ${Hr};
      border-color: ${ln};
    }

    :host(:${it.focusVisible}) .switch {
      outline-offset: 2px;
      outline: solid calc(${qt} * 1px) ${cr};
    }

    .checked-indicator {
      position: absolute;
      top: 5px;
      bottom: 5px;
      background: ${on};
      border-radius: calc(${Pt} * 1px);
      transition: all 0.2s ease-in-out;
    }

    .status-message {
      color: ${on};
      cursor: pointer;
      font-size: ${Wt};
      line-height: ${Ut};
    }

    :host([disabled]) .status-message,
    :host([readonly]) .status-message {
      cursor: ${it.disabledCursor};
    }

    .label {
      color: ${on};

      ${""} margin-inline-end: calc(${Mt} * 2px + 2px);
      font-size: ${Wt};
      line-height: ${Ut};
      cursor: pointer;
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    ::slotted([slot='checked-message']),
    ::slotted([slot='unchecked-message']) {
      margin-inline-start: calc(${Mt} * 2px + 2px);
    }

    :host([aria-checked='true']) .checked-indicator {
      background: ${ur};
    }

    :host([aria-checked='true']) .switch {
      background: ${ir};
      border-color: ${ir};
    }

    :host([aria-checked='true']:not([disabled])) .switch:hover {
      background: ${lr};
      border-color: ${lr};
    }

    :host([aria-checked='true']:not([disabled]))
      .switch:hover
      .checked-indicator {
      background: ${pr};
    }

    :host([aria-checked='true']:not([disabled])) .switch:active {
      background: ${sr};
      border-color: ${sr};
    }

    :host([aria-checked='true']:not([disabled]))
      .switch:active
      .checked-indicator {
      background: ${gr};
    }

    :host([aria-checked="true"]:${it.focusVisible}:not([disabled])) .switch {
      outline: solid calc(${qt} * 1px) ${cr};
    }

    .unchecked-message {
      display: block;
    }

    .checked-message {
      display: none;
    }

    :host([aria-checked='true']) .unchecked-message {
      display: none;
    }

    :host([aria-checked='true']) .checked-message {
      display: block;
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      .checked-indicator,
      :host(:not([disabled])) .switch:active .checked-indicator {
        forced-color-adjust: none;
        background: ${na.FieldText};
      }
      .switch {
        forced-color-adjust: none;
        background: ${na.Field};
        border-color: ${na.FieldText};
      }
      :host(:not([disabled])) .switch:hover {
        background: ${na.HighlightText};
        border-color: ${na.Highlight};
      }
      :host([aria-checked='true']) .switch {
        background: ${na.Highlight};
        border-color: ${na.Highlight};
      }
      :host([aria-checked='true']:not([disabled])) .switch:hover,
      :host(:not([disabled])) .switch:active {
        background: ${na.HighlightText};
        border-color: ${na.Highlight};
      }
      :host([aria-checked='true']) .checked-indicator {
        background: ${na.HighlightText};
      }
      :host([aria-checked='true']:not([disabled]))
        .switch:hover
        .checked-indicator {
        background: ${na.Highlight};
      }
      :host([disabled]) {
        opacity: 1;
      }
      :host(:${it.focusVisible}) .switch {
        border-color: ${na.Highlight};
        outline-offset: 2px;
        outline: solid calc(${qt} * 1px) ${na.FieldText};
      }
      :host([aria-checked="true"]:${it.focusVisible}:not([disabled])) .switch {
        outline: solid calc(${qt} * 1px) ${na.FieldText};
      }
      :host([disabled]) .checked-indicator {
        background: ${na.GrayText};
      }
      :host([disabled]) .switch {
        background: ${na.Field};
        border-color: ${na.GrayText};
      }
    `),new Sn(oa.css`
        .checked-indicator {
          left: 5px;
          right: calc(((${aa} / 2) + 1) * 1px);
        }

        :host([aria-checked='true']) .checked-indicator {
          left: calc(((${aa} / 2) + 1) * 1px);
          right: 5px;
        }
      `,oa.css`
        .checked-indicator {
          right: 5px;
          left: calc(((${aa} / 2) + 1) * 1px);
        }

        :host([aria-checked='true']) .checked-indicator {
          right: calc(((${aa} / 2) + 1) * 1px);
          left: 5px;
        }
      `));const ac=it.Switch.compose({baseName:"switch",template:it.switchTemplate,styles:nc,switch:`\n    <span class="checked-indicator" part="checked-indicator"></span>\n  `});const ic=(e,t)=>oa.css`
    ${(0,it.display)("block")} :host {
        box-sizing: border-box;
        font-size: ${Wt};
        line-height: ${Ut};
        padding: 0 calc((6 + (${Mt} * 2 * ${It})) * 1px);
    }
`;const lc=it.TabPanel.compose({baseName:"tab-panel",template:it.tabPanelTemplate,styles:ic});const sc=(e,t)=>oa.css`
    ${(0,it.display)("inline-flex")} :host {
      box-sizing: border-box;
      font-family: ${Ht};
      font-size: ${Wt};
      line-height: ${Ut};
      height: calc(${aa} * 1px);
      padding: calc(${Mt} * 5px) calc(${Mt} * 4px);
      color: ${en};
      fill: currentcolor;
      border-radius: 0 0 calc(${Pt} * 1px)
        calc(${Pt} * 1px);
      border: calc(${Et} * 1px) solid transparent;
      align-items: center;
      grid-row: 2;
      justify-content: center;
      cursor: pointer;
    }

    :host(:hover) {
      color: ${on};
      fill: currentcolor;
    }

    :host(:active) {
      color: ${on};
      fill: currentcolor;
    }

    :host([disabled]) {
      cursor: ${it.disabledCursor};
      opacity: ${_t};
    }

    :host([disabled]:hover) {
      color: ${en};
      background: ${Rr};
    }

    :host([aria-selected='true']) {
      background: ${Dr};
      color: ${on};
      fill: currentcolor;
    }

    :host([aria-selected='true']:hover) {
      background: ${Sr};
      color: ${on};
      fill: currentcolor;
    }

    :host([aria-selected='true']:active) {
      background: ${jr};
      color: ${on};
      fill: currentcolor;
    }

    :host(:${it.focusVisible}) {
      outline: none;
      border-color: ${cr};
      box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px)
        ${cr};
    }

    :host(:focus) {
      outline: none;
    }

    :host(.vertical) {
      justify-content: end;
      grid-column: 2;
      border-bottom-left-radius: 0;
      border-top-right-radius: calc(${Pt} * 1px);
    }

    :host(.vertical[aria-selected='true']) {
      z-index: 2;
    }

    :host(.vertical:hover) {
      color: ${on};
    }

    :host(.vertical:active) {
      color: ${on};
    }

    :host(.vertical:hover[aria-selected='true']) {
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        color: ${na.ButtonText};
        fill: currentcolor;
      }
      :host(:hover),
      :host(.vertical:hover),
      :host([aria-selected='true']:hover) {
        background: ${na.Highlight};
        color: ${na.HighlightText};
        fill: currentcolor;
      }
      :host([aria-selected='true']) {
        background: ${na.HighlightText};
        color: ${na.Highlight};
        fill: currentcolor;
      }
      :host(:${it.focusVisible}) {
        border-color: ${na.ButtonText};
        box-shadow: none;
      }
      :host([disabled]),
      :host([disabled]:hover) {
        opacity: 1;
        color: ${na.GrayText};
        background: ${na.ButtonFace};
      }
    `));const cc=it.Tab.compose({baseName:"tab",template:it.tabTemplate,styles:sc});const dc=(e,t)=>oa.css`
    ${(0,it.display)("grid")} :host {
      box-sizing: border-box;
      font-family: ${Ht};
      font-size: ${Wt};
      line-height: ${Ut};
      color: ${on};
      grid-template-columns: auto 1fr auto;
      grid-template-rows: auto 1fr;
    }

    .tablist {
      display: grid;
      grid-template-rows: auto auto;
      grid-template-columns: auto;
      position: relative;
      width: max-content;
      align-self: end;
      padding: calc(${Mt} * 4px) calc(${Mt} * 4px) 0;
      box-sizing: border-box;
    }

    .start,
    .end {
      align-self: center;
    }

    .activeIndicator {
      grid-row: 1;
      grid-column: 1;
      width: 100%;
      height: 4px;
      justify-self: center;
      background: ${ir};
      margin-top: 0;
      border-radius: calc(${Pt} * 1px)
        calc(${Pt} * 1px) 0 0;
    }

    .activeIndicatorTransition {
      transition: transform 0.01s ease-in-out;
    }

    .tabpanel {
      grid-row: 2;
      grid-column-start: 1;
      grid-column-end: 4;
      position: relative;
    }

    :host([orientation='vertical']) {
      grid-template-rows: auto 1fr auto;
      grid-template-columns: auto 1fr;
    }

    :host([orientation='vertical']) .tablist {
      grid-row-start: 2;
      grid-row-end: 2;
      display: grid;
      grid-template-rows: auto;
      grid-template-columns: auto 1fr;
      position: relative;
      width: max-content;
      justify-self: end;
      align-self: flex-start;
      width: 100%;
      padding: 0 calc(${Mt} * 4px)
        calc((${aa} - ${Mt}) * 1px) 0;
    }

    :host([orientation='vertical']) .tabpanel {
      grid-column: 2;
      grid-row-start: 1;
      grid-row-end: 4;
    }

    :host([orientation='vertical']) .end {
      grid-row: 3;
    }

    :host([orientation='vertical']) .activeIndicator {
      grid-column: 1;
      grid-row: 1;
      width: 4px;
      height: 100%;
      margin-inline-end: 0px;
      align-self: center;
      border-radius: calc(${Pt} * 1px) 0 0
        calc(${Pt} * 1px);
    }

    :host([orientation='vertical']) .activeIndicatorTransition {
      transition: transform 0.01s ease-in-out;
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      .activeIndicator,
      :host([orientation='vertical']) .activeIndicator {
        forced-color-adjust: none;
        background: ${na.Highlight};
      }
    `));const hc=it.Tabs.compose({baseName:"tabs",template:it.tabsTemplate,styles:dc});const uc=(e,t)=>oa.css`
    ${(0,it.display)("inline-block")} :host {
        font-family: ${Ht};
        outline: none;
        user-select: none;
    }

    .control {
        box-sizing: border-box;
        position: relative;
        color: ${on};
        background: ${zr};
        border-radius: calc(${Pt} * 1px);
        border: calc(${Et} * 1px) solid ${ir};
        height: calc(${La} * 2px);
        font: inherit;
        font-size: ${Wt};
        line-height: ${Ut};
        padding: calc(${Mt} * 2px + 1px);
        width: 100%;
        resize: none;
    }

    .control:hover:enabled {
        background: ${Lr};
        border-color: ${lr};
    }

    .control:active:enabled {
        background: ${Hr};
        border-color: ${sr};
    }

    .control:hover,
    .control:${it.focusVisible},
    .control:disabled,
    .control:active {
        outline: none;
    }

    :host(:focus-within) .control {
        border-color: ${Yr};
        box-shadow: 0 0 0 1px ${Yr} inset;
    }

    :host([appearance="filled"]) .control {
        background: ${Dr};
    }

    :host([appearance="filled"]:hover:not([disabled])) .control {
        background: ${Sr};
    }

    :host([resize="both"]) .control {
        resize: both;
    }

    :host([resize="horizontal"]) .control {
        resize: horizontal;
    }

    :host([resize="vertical"]) .control {
        resize: vertical;
    }

    .label {
        display: block;
        color: ${on};
        cursor: pointer;
        font-size: ${Wt};
        line-height: ${Ut};
        margin-bottom: 4px;
    }

    .label__hidden {
        display: none;
        visibility: hidden;
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
        cursor: ${it.disabledCursor};
    }
    :host([disabled]) {
        opacity: ${_t};
    }
    :host([disabled]) .control {
        border-color: ${nn};
    }

    :host([cols]){
        width: initial;
    }

    :host([rows]) .control {
        height: initial;
    }
 `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                :host([disabled]) {
                    opacity: 1;
                }
            `));class pc extends it.TextArea{constructor(){super(...arguments);this.appearance="outline"}}pa([oa.attr],pc.prototype,"appearance",void 0);const gc=pc.compose({baseName:"text-area",baseClass:it.TextArea,template:it.textAreaTemplate,styles:uc,shadowOptions:{delegatesFocus:true}});const bc=(e,t)=>oa.css`
    ${(0,it.display)("inline-block")} :host {
      font-family: ${Ht};
      outline: none;
      user-select: none;
    }

    .control {
      box-sizing: border-box;
      position: relative;
      color: ${on};
      background: ${zr};
      border-radius: calc(${Pt} * 1px);
      border: calc(${Et} * 1px) solid ${_r};
      height: calc(${aa} * 2px);
      font: inherit;
      font-size: ${Wt};
      line-height: ${Ut};
      padding: calc(${Mt} * 2px + 1px);
      width: 100%;
      resize: none;
    }

    .control:hover:enabled {
      background: ${Lr};
      border-color: ${Er};
    }

    .control:active:enabled {
      background: ${Hr};
      border-color: ${qr};
    }

    .control:hover,
    .control:${it.focusVisible},
    .control:disabled,
    .control:active {
      outline: none;
    }

    :host(:focus-within) .control {
      border-color: ${cr};
      box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px)
        ${cr};
    }

    :host([appearance='filled']) .control {
      background: ${Dr};
    }

    :host([appearance='filled']:hover:not([disabled])) .control {
      background: ${Sr};
    }

    :host([resize='both']) .control {
      resize: both;
    }

    :host([resize='horizontal']) .control {
      resize: horizontal;
    }

    :host([resize='vertical']) .control {
      resize: vertical;
    }

    .label {
      display: block;
      color: ${on};
      cursor: pointer;
      font-size: ${Wt};
      line-height: ${Ut};
      margin-bottom: 4px;
    }

    .label__hidden {
      display: none;
      visibility: hidden;
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
      cursor: ${it.disabledCursor};
    }
    :host([disabled]) {
      opacity: ${_t};
    }
    :host([disabled]) .control {
      border-color: ${nn};
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host([disabled]) {
        opacity: 1;
      }
    `));const fc=pc.compose({baseName:"text-area",baseClass:it.TextArea,template:it.textAreaTemplate,styles:bc,shadowOptions:{delegatesFocus:true}});const $c=(e,t)=>oa.css`
    ${(0,it.display)("inline-block")} :host {
        font-family: ${Ht};
        outline: none;
        user-select: none;
    }

    .root {
        box-sizing: border-box;
        position: relative;
        display: flex;
        flex-direction: row;
        color: ${on};
        background: ${zr};
        border-radius: calc(${Pt} * 1px);
        border: calc(${Et} * 1px) solid ${ir};
        height: calc(${La} * 1px);
        align-items: baseline;
    }

    .control {
        -webkit-appearance: none;
        font: inherit;
        background: transparent;
        border: 0;
        color: inherit;
        height: calc(100% - 4px);
        width: 100%;
        margin-top: auto;
        margin-bottom: auto;
        border: none;
        padding: 0 calc(${Mt} * 2px + 1px);
        font-size: ${Wt};
        line-height: ${Ut};
    }

    .control:hover,
    .control:${it.focusVisible},
    .control:disabled,
    .control:active {
        outline: none;
    }

    .label {
        display: block;
        color: ${on};
        cursor: pointer;
        font-size: ${Wt};
        line-height: ${Ut};
        margin-bottom: 4px;
    }

    .label__hidden {
        display: none;
        visibility: hidden;
    }

    .start,
    .control,
    .end {
        align-self: center;
    }

    .start,
    .end {
        display: flex;
        margin: auto;
        fill: currentcolor;
    }

    ::slotted(svg) {
        /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
        width: 16px;
        height: 16px;
    }

    .start {
        margin-inline-start: 11px;
    }

    .end {
        margin-inline-end: 11px;
    }

    :host(:hover:not([disabled])) .root {
        background: ${Lr};
        border-color: ${lr};
    }

    :host(:active:not([disabled])) .root {
        background: ${Lr};
        border-color: ${sr};
    }

    :host(:focus-within:not([disabled])) .root {
        border-color: ${Yr};
        box-shadow: 0 0 0 calc(${qt} * 1px) ${Yr} inset;
    }

    :host([appearance="filled"]) .root {
        background: ${Dr};
    }

    :host([appearance="filled"]:hover:not([disabled])) .root {
        background: ${Sr};
    }

    :host([disabled]) .label,
    :host([readonly]) .label,
    :host([readonly]) .control,
    :host([disabled]) .control {
        cursor: ${it.disabledCursor};
    }

    :host([disabled]) {
        opacity: ${_t};
    }

    :host([disabled]) .control {
        border-color: ${nn};
    }
`.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                .root,
                :host([appearance="filled"]) .root {
                    forced-color-adjust: none;
                    background: ${za.Field};
                    border-color: ${za.FieldText};
                }
                :host(:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover:not([disabled])) .root,
                :host([appearance="filled"]:hover) .root {
                    background: ${za.Field};
                    border-color: ${za.Highlight};
                }
                .start,
                .end {
                    fill: currentcolor;
                }
                :host([disabled]) {
                    opacity: 1;
                }
                :host([disabled]) .root,
                :host([appearance="filled"]:hover[disabled]) .root {
                    border-color: ${za.GrayText};
                    background: ${za.Field};
                }
                :host(:focus-within:enabled) .root {
                    border-color: ${za.Highlight};
                    box-shadow: 0 0 0 1px ${za.Highlight} inset;
                }
                input::placeholder {
                    color: ${za.GrayText};
                }
            `));class xc extends it.TextField{constructor(){super(...arguments);this.appearance="outline"}}pa([oa.attr],xc.prototype,"appearance",void 0);const mc=xc.compose({baseName:"text-field",baseClass:it.TextField,template:it.textFieldTemplate,styles:$c,shadowOptions:{delegatesFocus:true}});const vc=(e,t)=>oa.css`
  ${ss}

  .start,
    .end {
    display: flex;
  }
`;const yc=xc.compose({baseName:"text-field",baseClass:it.TextField,template:it.textFieldTemplate,styles:vc,shadowOptions:{delegatesFocus:true}});const wc=(e,t)=>oa.css`
        ${(0,it.display)("inline-flex")} :host {
            --toolbar-item-gap: calc(
                (var(--design-unit) + calc(var(--density) + 2)) * 1px
            );
            background-color: ${rr};
            border-radius: calc(${Pt} * 1px);
            fill: currentcolor;
            padding: var(--toolbar-item-gap);
        }

        :host(${it.focusVisible}) {
            outline: calc(${Et} * 1px) solid ${sn};
        }

        .positioning-region {
            align-items: flex-start;
            display: inline-flex;
            flex-flow: row wrap;
            justify-content: flex-start;
        }

        :host([orientation="vertical"]) .positioning-region {
            flex-direction: column;
        }

        ::slotted(:not([slot])) {
            flex: 0 0 auto;
            margin: 0 var(--toolbar-item-gap);
        }

        :host([orientation="vertical"]) ::slotted(:not([slot])) {
            margin: var(--toolbar-item-gap) 0;
        }

        .start,
        .end {
            display: flex;
            margin: auto;
            margin-inline: 0;
        }

        ::slotted(svg) {
            /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
            width: 16px;
            height: 16px;
        }
    `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
            :host(:${it.focusVisible}) {
                box-shadow: 0 0 0 calc(${qt} * 1px) ${za.Highlight};
                color: ${za.ButtonText};
                forced-color-adjust: none;
            }
        `));class kc extends it.Toolbar{connectedCallback(){super.connectedCallback();const e=(0,it.composedParent)(this);if(e){rr.setValueFor(this,(t=>Ur.getValueFor(t).evaluate(t,rr.getValueFor(e))))}}}const Fc=kc.compose({baseName:"toolbar",baseClass:it.Toolbar,template:it.toolbarTemplate,styles:wc,shadowOptions:{delegatesFocus:true}});const Tc=(e,t)=>oa.css`
    ${(0,it.display)("inline-flex")} :host {
      --toolbar-item-gap: calc(
        (var(--design-unit) + calc(var(--density) + 2)) * 1px
      );
      background-color: ${rr};
      border-radius: calc(${Pt} * 1px);
      fill: currentcolor;
      padding: var(--toolbar-item-gap);
    }

    :host(${it.focusVisible}) {
      outline: calc(${Et} * 1px) solid ${cr};
    }

    .positioning-region {
      align-items: flex-start;
      display: inline-flex;
      flex-flow: row wrap;
      justify-content: flex-start;
      width: 100%;
      height: 100%;
    }

    :host([orientation='vertical']) .positioning-region {
      flex-direction: column;
    }

    ::slotted(:not([slot])) {
      flex: 0 0 auto;
      margin: 0 var(--toolbar-item-gap);
    }

    :host([orientation='vertical']) ::slotted(:not([slot])) {
      margin: var(--toolbar-item-gap) 0;
    }

    .start,
    .end {
      display: flex;
      margin: auto;
      margin-inline: 0;
    }

    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
    }
  `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host(:${it.focusVisible}) {
        box-shadow: 0 0 0 calc(${qt} * 1px)
          ${na.Highlight};
        color: ${na.ButtonText};
        forced-color-adjust: none;
      }
    `));const Cc=kc.compose({baseName:"toolbar",baseClass:it.Toolbar,template:it.toolbarTemplate,styles:Tc,shadowOptions:{delegatesFocus:true}});const Vc=(e,t)=>{const o=e.tagFor(it.AnchoredRegion);return oa.css`
            :host {
                contain: size;
                overflow: visible;
                height: 0;
                width: 0;
            }

            .tooltip {
                box-sizing: border-box;
                border-radius: calc(${Pt} * 1px);
                border: calc(${Et} * 1px) solid ${Yr};
                box-shadow: 0 0 0 1px ${Yr} inset;
                background: ${Dr};
                color: ${on};
                padding: 4px;
                height: fit-content;
                width: fit-content;
                font-family: ${Ht};
                font-size: ${Wt};
                line-height: ${Ut};
                white-space: nowrap;
                /* TODO: a mechanism to manage z-index across components
                    https://github.com/microsoft/fast/issues/3813 */
                z-index: 10000;
            }

            ${o} {
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: visible;
                flex-direction: row;
            }

            ${o}.right,
            ${o}.left {
                flex-direction: column;
            }

            ${o}.top .tooltip {
                margin-bottom: 4px;
            }

            ${o}.bottom .tooltip {
                margin-top: 4px;
            }

            ${o}.left .tooltip {
                margin-right: 4px;
            }

            ${o}.right .tooltip {
                margin-left: 4px;
            }

            ${o}.top.left .tooltip,
            ${o}.top.right .tooltip {
                margin-bottom: 0px;
            }

            ${o}.bottom.left .tooltip,
            ${o}.bottom.right .tooltip {
                margin-top: 0px;
            }

            ${o}.top.left .tooltip,
            ${o}.bottom.left .tooltip {
                margin-right: 0px;
            }

            ${o}.top.right .tooltip,
            ${o}.bottom.right .tooltip {
                margin-left: 0px;
            }

        `.withBehaviors((0,it.forcedColorsStylesheetBehavior)(oa.css`
                :host([disabled]) {
                    opacity: 1;
                }
            `))};const Dc=it.Tooltip.compose({baseName:"tooltip",template:it.tooltipTemplate,styles:Vc});const Sc=oa.css`
  .expand-collapse-glyph {
    transform: rotate(0deg);
  }
  :host(.nested) .expand-collapse-button {
    left: var(
      --expand-collapse-button-nested-width,
      calc(${aa} * -1px)
    );
  }
  :host([selected])::after {
    left: calc(${qt} * 1px);
  }
  :host([expanded]) > .positioning-region .expand-collapse-glyph {
    transform: rotate(90deg);
  }
`;const jc=oa.css`
  .expand-collapse-glyph {
    transform: rotate(180deg);
  }
  :host(.nested) .expand-collapse-button {
    right: var(
      --expand-collapse-button-nested-width,
      calc(${aa} * -1px)
    );
  }
  :host([selected])::after {
    right: calc(${qt} * 1px);
  }
  :host([expanded]) > .positioning-region .expand-collapse-glyph {
    transform: rotate(90deg);
  }
`;const Bc=oa.cssPartial`((${Nt} / 2) * ${Mt}) + ((${Mt} * ${It}) / 2)`;const Oc=it.DesignToken.create("tree-item-expand-collapse-hover").withDefault((e=>{const t=Ar.getValueFor(e);return t.evaluate(e,t.evaluate(e).hover).hover}));const zc=it.DesignToken.create("tree-item-expand-collapse-selected-hover").withDefault((e=>{const t=Vr.getValueFor(e);const o=Ar.getValueFor(e);return o.evaluate(e,t.evaluate(e).rest).hover}));const Lc=(e,t)=>oa.css`
    ${(0,it.display)("block")} :host {
      contain: content;
      position: relative;
      outline: none;
      color: ${on};
      background: ${Rr};
      cursor: pointer;
      font-family: ${Ht};
      --expand-collapse-button-size: calc(${aa} * 1px);
      --tree-item-nested-width: 0;
    }

    :host(:focus) > .positioning-region {
      outline: none;
    }

    :host(:focus) .content-region {
      outline: none;
    }

    :host(:${it.focusVisible}) .positioning-region {
      border-color: ${cr};
      box-shadow: 0 0 0 calc((${qt} - ${Et}) * 1px)
        ${cr} inset;
      color: ${on};
    }

    .positioning-region {
      display: flex;
      position: relative;
      box-sizing: border-box;
      border: transparent calc(${Et} * 1px) solid;
      border-radius: calc(${Pt} * 1px);
      height: calc((${aa} + 1) * 1px);
    }

    .positioning-region::before {
      content: '';
      display: block;
      width: var(--tree-item-nested-width);
      flex-shrink: 0;
    }

    .positioning-region:hover {
      background: ${Pr};
    }

    .positioning-region:active {
      background: ${Ir};
    }

    .content-region {
      display: inline-flex;
      align-items: center;
      white-space: nowrap;
      width: 100%;
      min-width: 0;
      height: calc(${aa} * 1px);
      margin-inline-start: calc(${Mt} * 2px + 8px);
      font-size: ${Wt};
      line-height: ${Ut};
      font-weight: 400;
    }

    .items {
      display: none;
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      font-size: calc(1em + (${Mt} + 16) * 1px);
    }

    .expand-collapse-button {
      background: none;
      border: none;
      outline: none;
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: calc((${Bc} + (${Mt} * 2)) * 1px);
      height: calc((${Bc} + (${Mt} * 2)) * 1px);
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      margin-left: 6px;
      margin-right: 6px;
    }

    .expand-collapse-glyph {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
      transition: transform 0.1s linear;

      pointer-events: none;
      fill: currentcolor;
    }

    .start,
    .end {
      display: flex;
      fill: currentcolor;
    }

    ::slotted(svg) {
      /* TODO: adaptive typography https://github.com/microsoft/fast/issues/2432 */
      width: 16px;
      height: 16px;
    }

    .start {
      /* TODO: horizontalSpacing https://github.com/microsoft/fast/issues/2766 */
      margin-inline-end: calc(${Mt} * 2px + 2px);
    }

    .end {
      /* TODO: horizontalSpacing https://github.com/microsoft/fast/issues/2766 */
      margin-inline-start: calc(${Mt} * 2px + 2px);
    }

    :host([expanded]) > .items {
      display: block;
    }

    :host([disabled]) .content-region {
      opacity: ${_t};
      cursor: ${it.disabledCursor};
    }

    :host(.nested) .content-region {
      position: relative;
      margin-inline-start: var(--expand-collapse-button-size);
    }

    :host(.nested) .expand-collapse-button {
      position: absolute;
    }

    :host(.nested) .expand-collapse-button:hover {
      background: ${Oc};
    }

    :host([selected]) .positioning-region {
      background: ${Dr};
    }

    :host([selected]) .expand-collapse-button:hover {
      background: ${zc};
    }

    :host([selected])::after {
      /* The background needs to be calculated based on the selected background state
            for this control. We currently have no way of changing that, so setting to
            accent-foreground-rest for the time being */
      background: ${kr};
      border-radius: calc(${Pt} * 1px);
      content: '';
      display: block;
      position: absolute;
      top: calc((${aa} / 4) * 1px);
      width: 3px;
      height: calc((${aa} / 2) * 1px);
    }

    ::slotted(${e.tagFor(it.TreeItem)}) {
      --tree-item-nested-width: 1em;
      --expand-collapse-button-nested-width: calc(${aa} * -1px);
    }
  `.withBehaviors(new Sn(Sc,jc),(0,it.forcedColorsStylesheetBehavior)(oa.css`
      :host {
        forced-color-adjust: none;
        border-color: transparent;
        background: ${na.Field};
        color: ${na.FieldText};
      }
      :host .content-region .expand-collapse-glyph {
        fill: ${na.FieldText};
      }
      :host .positioning-region:hover,
      :host([selected]) .positioning-region {
        background: ${na.Highlight};
      }
      :host .positioning-region:hover .content-region,
      :host([selected]) .positioning-region .content-region {
        color: ${na.HighlightText};
      }
      :host .positioning-region:hover .content-region .expand-collapse-glyph,
      :host .positioning-region:hover .content-region .start,
      :host .positioning-region:hover .content-region .end,
      :host([selected]) .content-region .expand-collapse-glyph,
      :host([selected]) .content-region .start,
      :host([selected]) .content-region .end {
        fill: ${na.HighlightText};
      }
      :host([selected])::after {
        background: ${na.Field};
      }
      :host(:${it.focusVisible}) .positioning-region {
        border-color: ${na.FieldText};
        box-shadow: 0 0 0 2px inset ${na.Field};
        color: ${na.FieldText};
      }
      :host([disabled]) .content-region,
      :host([disabled]) .positioning-region:hover .content-region {
        opacity: 1;
        color: ${na.GrayText};
      }
      :host([disabled]) .content-region .expand-collapse-glyph,
      :host([disabled]) .content-region .start,
      :host([disabled]) .content-region .end,
      :host([disabled])
        .positioning-region:hover
        .content-region
        .expand-collapse-glyph,
      :host([disabled]) .positioning-region:hover .content-region .start,
      :host([disabled]) .positioning-region:hover .content-region .end {
        fill: ${na.GrayText};
      }
      :host([disabled]) .positioning-region:hover {
        background: ${na.Field};
      }
      .expand-collapse-glyph,
      .start,
      .end {
        fill: ${na.FieldText};
      }
      :host(.nested) .expand-collapse-button:hover {
        background: ${na.Field};
      }
      :host(.nested) .expand-collapse-button:hover .expand-collapse-glyph {
        fill: ${na.FieldText};
      }
    `));const Hc=it.TreeItem.compose({baseName:"tree-item",template:it.treeItemTemplate,styles:Lc,expandCollapseGlyph:`\n        <svg\n            viewBox="0 0 16 16"\n            xmlns="http://www.w3.org/2000/svg"\n            class="expand-collapse-glyph"\n        >\n            <path\n                d="M5.00001 12.3263C5.00124 12.5147 5.05566 12.699 5.15699 12.8578C5.25831 13.0167 5.40243 13.1437 5.57273 13.2242C5.74304 13.3047 5.9326 13.3354 6.11959 13.3128C6.30659 13.2902 6.4834 13.2152 6.62967 13.0965L10.8988 8.83532C11.0739 8.69473 11.2153 8.51658 11.3124 8.31402C11.4096 8.11146 11.46 7.88966 11.46 7.66499C11.46 7.44033 11.4096 7.21853 11.3124 7.01597C11.2153 6.81341 11.0739 6.63526 10.8988 6.49467L6.62967 2.22347C6.48274 2.10422 6.30501 2.02912 6.11712 2.00691C5.92923 1.9847 5.73889 2.01628 5.56823 2.09799C5.39757 2.17969 5.25358 2.30817 5.153 2.46849C5.05241 2.62882 4.99936 2.8144 5.00001 3.00369V12.3263Z"\n            />\n        </svg>\n    `});const Nc=(e,t)=>oa.css`
    ${(0,it.display)("flex")} :host {
        flex-direction: column;
        align-items: stretch;
        min-width: fit-content;
        font-size: 0;
    }

    :host:focus-visible {
        outline: none;
    }
`;const Ac=it.TreeView.compose({baseName:"tree-view",template:it.treeViewTemplate,styles:Nc});const Rc={jpAccordion:sa,jpAccordionItem:la,jpAnchor:qa,jpAnchoredRegion:Ua,jpAvatar:ri,jpBadge:ai,jpBreadcrumb:li,jpBreadcrumbItem:ci,jpButton:Yi,jpCard:rl,jpCheckbox:al,jpCombobox:ul,jpDataGrid:xl,jpDataGridCell:fl,jpDataGridRow:$l,jpDateField:hs,jpDialog:ps,jpDivider:bs,jpListbox:$s,jpMenu:ms,jpMenuItem:ys,jpNumberField:Cs,jpOption:Ds,jpProgress:js,jpProgressRing:Os,jpRadio:Ls,jpRadioGroup:Ns,jpSearch:Ws,jpSelect:Xs,jpSlider:Ys,jpSliderLabel:rc,jpSwitch:ac,jpTab:cc,jpTabPanel:lc,jpTabs:hc,jpTextArea:fc,jpTextField:yc,jpToolbar:Cc,jpTooltip:Dc,jpTreeItem:Hc,jpTreeView:Ac,register(e,...t){if(!e){return}for(const o in this){if(o==="register"){continue}this[o]().register(e,...t)}}}},62899:(e,t,o)=>{o.d(t,{i:()=>r});const r={horizontal:"horizontal",vertical:"vertical"}},42586:(e,t,o)=>{o.d(t,{N:()=>r});var r;(function(e){e["ltr"]="ltr";e["rtl"]="rtl"})(r||(r={}))}}]);